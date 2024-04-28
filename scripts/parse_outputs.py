import sys
before_laser_dict = dict()
with_laser_dict = dict()
higher_laser_dict = dict()

if(sys.argv[1] == "counterfact"):
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
if(sys.argv[1] == "fever"):
    output = open("fever_results.txt", "w")
    with open("fever_output1.txt") as b:
        for line in b:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            question = temp[1]
            true_answer = temp[2]
            true_logprob = temp[3]
            false_logprob = temp[4]
            tokens_str = temp[5]
            before_laser_dict[question] = [is_correct, true_answer, true_logprob, false_logprob, tokens_str]
    with open("fever_output2.txt") as w:
        for line in w:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            question = temp[1]
            true_answer = temp[2]
            true_logprob = temp[3]
            false_logprob = temp[4]
            tokens_str = temp[5]
            with_laser_dict[question] = [is_correct, true_answer, true_logprob, false_logprob, tokens_str] 
    with open("fever_output3.txt") as h:
        for line in h:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            question = temp[1]
            true_answer = temp[2]
            true_logprob = temp[3]
            false_logprob = temp[4]
            tokens_str = temp[5]
            higher_laser_dict[question] = [is_correct, true_answer, true_logprob, false_logprob, tokens_str]   
    false_count = 0
    true_count = 0
    before_laser_incorrect = 0
    with_laser_incorrect = 0
    higher_laser_incorrect = 0
    before_laser_tokens = 0
    with_laser_tokens = 0
    higher_laser_tokens = 0
    for key in before_laser_dict:
        if before_laser_dict[key][0] == '0' and with_laser_dict[key][0] == '1':
            output.write(f"No LASER: {before_laser_dict[key][4][0]}\t\tLASER: {with_laser_dict[key][4][0]}\t\tHigher Order LASER: {higher_laser_dict[key][4][0]}\t\tQuestion: {key}\t\tTrue Ans: {with_laser_dict[key][1]}\t\tTokens before: {before_laser_dict[key][4]}\t\tTokens after: {with_laser_dict[key][4]}\t\tTokens high: {higher_laser_dict[key][4]}\n")
            if higher_laser_dict[key][4][0] == 'f':
                false_count += 1
            else:
                true_count += 1
        if before_laser_dict[key][0] == '0':
            before_laser_incorrect += 1
        if with_laser_dict[key][0] == '0':
            with_laser_incorrect+=1
        if higher_laser_dict[key][0] == '0':
            higher_laser_incorrect+=1
        for word in before_laser_dict[key][4].split(','):
            if word != 'true' and word != 'false':
                before_laser_tokens+=1
        for word in with_laser_dict[key][4].split(','):
            if word != 'true' and word != 'false':
                with_laser_tokens+=1
        for word in higher_laser_dict[key][4].split(','):
            if word != 'true' and word != 'false':
                higher_laser_tokens+=1

    print(f"False: {false_count}")
    print(f"True: {true_count}")
    print(f"Before laser incorrect: {before_laser_incorrect}")
    print(f"With laser incorrect: {with_laser_incorrect}")
    print(f"Higher laser incorrect: {higher_laser_incorrect}")
    print(f"Before laser tokens that are not true/false: {before_laser_tokens}")
    print(f"With laser tokens that are not true/false: {with_laser_tokens}")
    print(f"Higher laser tokens that are not true/false: {higher_laser_tokens}")
    
if sys.argv[1] == 'bios':
    output = open("bios_results.txt", "w")
    with open("bios_output1.txt") as b:
        for line in b:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            pred_answer = temp[1]
            true_answer = temp[2]
            tokens_str = temp[3]
            question = temp[4]
            before_laser_dict[question] = [is_correct, pred_answer, true_answer, tokens_str]
    with open("bios_output2.txt") as w:
        for line in w:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            pred_answer = temp[1]
            true_answer = temp[2]
            tokens_str = temp[3]
            question = temp[4]
            with_laser_dict[question] = [is_correct, pred_answer, true_answer, tokens_str] 
    with open("bios_output3.txt") as h:
        for line in h:
            temp = (line.rstrip('\n')).split('\t')
            is_correct = temp[0]
            pred_answer = temp[1]
            true_answer = temp[2]
            tokens_str = temp[3]
            question = temp[4]
            higher_laser_dict[question] = [is_correct, pred_answer, true_answer, tokens_str]   
    before_laser_incorrect = 0
    with_laser_incorrect = 0
    higher_laser_incorrect = 0
    for key in before_laser_dict:
        if before_laser_dict[key][0] == '0' and with_laser_dict[key][0] == '1':
            output.write(f"No LASER: {before_laser_dict[key][1]}\t\tLASER: {with_laser_dict[key][1]}\t\tHigher Order LASER: {higher_laser_dict[key][1]}\t\tQuestion: {key}\t\tTrue Ans: {with_laser_dict[key][2]}\n")
        if before_laser_dict[key][0] == '0':
            before_laser_incorrect += 1
        if with_laser_dict[key][0] == '0':
            with_laser_incorrect+=1
        if higher_laser_dict[key][0] == '0':
            higher_laser_incorrect+=1
    print(f"Before laser incorrect: {before_laser_incorrect}")
    print(f"With laser incorrect: {with_laser_incorrect}")
    print(f"Higher laser incorrect: {higher_laser_incorrect}")