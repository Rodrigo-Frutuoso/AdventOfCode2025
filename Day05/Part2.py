import os

def solve():
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_path, "input.txt")
    with open(input_file, "r") as f:
        content = f.read().strip()
    
    parts = content.split("\n\n")
    ranges_section = parts[0]
    
    ranges = []
    for line in ranges_section.split("\n"):
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    
    ranges.sort()
    
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    total_fresh = sum(end - start + 1 for start, end in merged)
    
    print(total_fresh)

if __name__ == "__main__":
    solve()
