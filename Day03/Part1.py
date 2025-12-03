def find_max_joltage(bank):
    max_joltage = 0
    n = len(bank)
    for i in range(n):
        for j in range(i + 1, n):
            joltage = int(bank[i]) * 10 + int(bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage

with open('input.txt') as f:
    lines = f.read().strip().split('\n')

total = 0
for line in lines:
    total += find_max_joltage(line)

print(f'Total: {total}')
