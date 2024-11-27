py_file = './THE2.py'
case_file = './cases.txt'

import subprocess
outputs = []
true_count = 0
with open(case_file, 'r') as file:
    for count,line in enumerate(file):
        process = subprocess.Popen(
        ['python', py_file], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True)
        case = eval(line.strip())
        money = case['money']
        _ = case.pop('money')

        tax = case['tax']
        _ = case.pop('tax')

        inputs  = f"{case}\n{money}"
        output, _ = process.communicate(input=inputs)
        output = output.replace('\n','')
        tf = tax==output
        if tf:
            true_count += 1
        print(f"CASE {count} | {tf} | {output} | {tax}")
print("FINISHED")
print(f"SCORE {true_count} / {5184}")
input()
