import os

def solve():
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_path, "input.txt")

    with open(input_file, "r") as f:
        lines = f.readlines()
    
    lines = [line.rstrip('\n') for line in lines]
    operator_line = lines[-1]
    number_lines = lines[:-1]
    max_width = max(len(line) for line in lines)
    lines = [line.ljust(max_width) for line in lines]
    operator_line = lines[-1]
    number_lines = lines[:-1]
    num_cols = max_width

    problems = []
    current_problem_start = None

    for col in range(num_cols):
        has_content = False
        for row in number_lines:
            if col < len(row) and row[col] != ' ':
                has_content = True
                break
        if col < len(operator_line) and operator_line[col] != ' ':
            has_content = True
        if has_content:
            if current_problem_start is None:
                current_problem_start = col
        else:
            if current_problem_start is not None:
                problems.append((current_problem_start, col - 1))
                current_problem_start = None
    if current_problem_start is not None:
        problems.append((current_problem_start, num_cols - 1))
    
    grand_total = 0

    for start_col, end_col in problems:
        operator = None
        for col in range(start_col, end_col + 1):
            if operator_line[col] in '+*':
                operator = operator_line[col]
                break
        if operator is None:
            continue

        numbers = []
        for col in range(end_col, start_col - 1, -1):
            digits = []
            for row in number_lines:
                char = row[col] if col < len(row) else ' '
                if char.isdigit():
                    digits.append(char)
            if digits:
                num = int(''.join(digits))
                numbers.append(num)
        
        if operator == '+':
            result = sum(numbers)
        else:
            result = 1
            for num in numbers:
                result *= num
        
        grand_total += result

    print(grand_total)

if __name__ == "__main__":
    solve()
