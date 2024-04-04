before_laser_dict = dict()
with_laser_dict = dict()
higher_laser_dict = dict()

output = open("counterfact_results.txt", "w")

with open("counterfact_output1.txt") as b:
    for line in b:
        temp = (line.rstrip('\n')).split('\t')
        is_correct = temp[0]
        question = temp[1]
        true_answer = temp[2]
        pred_answer = temp[3]
        before_laser_dict[question] = [is_correct, pred_answer]
with open("counterfact_output2.txt") as w:
    for line in w:
        temp = (line.rstrip('\n')).split('\t')
        is_correct = temp[0]
        question = temp[1]
        true_answer = temp[2]
        pred_answer = temp[3]
        with_laser_dict[question] = [is_correct, pred_answer]
with open("counterfact_output3.txt") as h:
    for line in h:
        temp = (line.rstrip('\n')).split('\t')
        is_correct = temp[0]
        question = temp[1]
        true_answer = temp[2]
        pred_answer = temp[3]
        higher_laser_dict[question] = [is_correct, pred_answer]

for key in before_laser_dict:
    if before_laser_dict[key][0] == '0' and with_laser_dict[key][0] == '1':
        output.write(f"No LASER: {before_laser_dict[key][1]}\t\tLASER: {with_laser_dict[key][1]}\t\tHigher Order LASER: {higher_laser_dict[key][1]}\t\tQuestion: {key}\n")

output.close()   