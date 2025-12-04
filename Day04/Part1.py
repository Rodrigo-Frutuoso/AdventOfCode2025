import os

def solve():
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_path, "input.txt")

    with open(input_file, "r") as f:
        grid = [line.strip() for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    accessible_count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    print(accessible_count)

if __name__ == "__main__":
    solve()
