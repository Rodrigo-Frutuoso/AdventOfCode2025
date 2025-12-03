import os

def find_max_joltage(bank, num_digits=12):
    n = len(bank)
    result = []
    start = 0
    for i in range(num_digits):
        remaining_to_pick = num_digits - i
        end = n - remaining_to_pick + 1
        max_digit = '0'
        max_pos = start
        for pos in range(start, end):
            if bank[pos] > max_digit:
                max_digit = bank[pos]
                max_pos = pos
        result.append(max_digit)
        start = max_pos + 1
    return int(''.join(result))

script_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_path, "input.txt")

with open(input_file) as f:
    lines = f.read().strip().split('\n')

total = 0
for line in lines:
    total += find_max_joltage(line, 12)

print(f'Total: {total}')
