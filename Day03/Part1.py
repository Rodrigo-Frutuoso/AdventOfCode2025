import os

def find_max_joltage(bank):
    max_joltage = 0
    n = len(bank)
    for i in range(n):
        for j in range(i + 1, n):
            joltage = int(bank[i]) * 10 + int(bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage

script_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_path, "input.txt")

with open(input_file) as f:
    lines = f.read().strip().split('\n')

total = 0
for line in lines:
    total += find_max_joltage(line)

print(f'Total: {total}')
