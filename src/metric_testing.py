import subprocess
import sys

params = {"counterfact": ["fc_in", 27, 9.9], 
          "hotpot": ["fc_in", 27, 9], 
          "fever": ["fc_in", 24, 9.9], 
          "bios": ["fc_in", 14, 9.9], 
          "bios_profession": ["fc_in", 18, 9.9],
          "bbh": ["fc_in", 26, 9.9],
          "truthfulqa": ["fc_in", 7, 2],
          "bbh_qa": ["fc_in", 27, 9]}

file1_params = params[sys.argv[1]]
file2_params = params[sys.argv[2]]
file3_params = params[sys.argv[3]]
intervention_file1 = f"intervention_gptj_{sys.argv[1]}.py"
intervention_file2 = f"intervention_gptj_{sys.argv[2]}.py"
intervention_file3 = f"intervention_gptj_{sys.argv[3]}.py"

subprocess.run(['python3', intervention_file1, '--lname', file1_params[0], '--lnum', file1_params[1], '--rate', file1_params[2]])
subprocess.run(['python3', intervention_file2, '--lname', file1_params[0], '--lnum', file1_params[1], '--rate', file1_params[2]])
subprocess.run(['python3', intervention_file3, '--lname', file1_params[0], '--lnum', file1_params[1], '--rate', file1_params[2]])