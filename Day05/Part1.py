import os

def solve():
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_path, "input.txt")
    with open(input_file, "r") as f:
        content = f.read().strip()
    
    parts = content.split("\n\n")
    ranges_section = parts[0]
    ingredients_section = parts[1]
    
    ranges = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    
    ingredients = [int(x) for x in ingredients_section.split("\n")]
    
    fresh_count = 0
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                fresh_count += 1
                break 
    
    print(fresh_count)

if __name__ == "__main__":
    solve()
    