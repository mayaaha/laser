import torch
import numpy as np
import matplotlib.pyplot as plt


# Helper functions for abs weight pruning
def sorted_mat(matrix):
    temp = list(abs(matrix).flatten())
    temp.sort()
    return temp


def prune(matrix, mat_sort, to_prune):
    if to_prune != 0:
        alpha = mat_sort[int(to_prune * 0.1 * len(mat_sort))]
        matrix[abs(matrix) <= alpha] = 0
    return matrix


def rank(matrix):
    np_matrix = np.array(matrix)
    return np.linalg.matrix_rank(np_matrix)/min(list(np_matrix.shape))


# What percentage can be pruned by weight
def sparsity(matrix, alpha):
    abs_matrix = abs(matrix)
    filtered_matrix = abs_matrix[abs_matrix < alpha]
    return len(filtered_matrix)/matrix.size


def viz_rank_change(rank_list,name):
    fig = plt.figure()
    plt.plot(rank_list)
    plt.savefig(name)


# Helper functions for rank reduction
def do_low_rank(weight, k, debug=False, niter=2):
    assert weight.ndim == 2

    max_rank = min(weight.shape[0], weight.shape[1])
    desired_rank = int(max_rank * k)

    if debug:
        print(f"Shape is {weight.shape} and shape is {weight.dtype} => desired rank {desired_rank}")

    results = torch.svd_lowrank(weight,
                                q=desired_rank,
                                niter=niter)
    weight_approx = results[0] @ torch.diag(results[1]) @ results[2].T

    if debug:
        print(f"New matrix has shape {weight_approx.shape}")

    assert weight_approx.shape[0] == weight.shape[0] and weight_approx.shape[1] == weight.shape[1]
    weight_approx = torch.nn.Parameter(weight_approx)

    return weight_approx

def do_high_rank(weight, k, debug=False):
    assert weight.ndim == 2

    # Perform full SVD
    U, S, V = torch.svd(weight)

    # Determine the total number of singular values
    total_singular_values = S.shape[0]
    
    # Calculate the number of smallest singular values to keep
    desired_rank = int(total_singular_values * k)

    if debug:
        print(f"Shape is {weight.shape}, Data type is {weight.dtype}, Total singular values {total_singular_values}, Desired rank {desired_rank}")

    # Keep only the 'k' smallest singular values and corresponding vectors
    U_small = U[:, -desired_rank:]
    S_small = S[-desired_rank:]
    V_small = V[:, -desired_rank:]

    # Reconstruct the matrix using these smallest components
    weight_approx = U_small @ torch.diag(S_small) @ V_small.T

    if debug:
        print(f"New matrix has shape {weight_approx.shape}")

    # Check that the reconstruction is the same shape as the input
    assert weight_approx.shape[0] == weight.shape[0] and weight_approx.shape[1] == weight.shape[1]
    
    # Wrap the approximated weight matrix as a torch.nn.Parameter if needed for training
    weight_approx = torch.nn.Parameter(weight_approx)

    return weight_approx