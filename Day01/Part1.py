import os

# Caminho do ficheiro na mesma pasta do script
script_path = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_path, "input.txt")

position = 50
zero_count = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("L") or line.startswith("R"):
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                position = (position + distance) % 100
            else:
                position = (position - distance) % 100
                if position < 0:
                    position += 100

            if position == 0:
                zero_count += 1

print(f"The password is: {zero_count}")
