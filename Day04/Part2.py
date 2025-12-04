import os

def solve():
    script_path = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_path, "input.txt")

    with open(input_file, "r") as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    def count_adjacent_rolls(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                count += 1
        return count
    
    def find_accessible_rolls():
        accessible = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@' and count_adjacent_rolls(r, c) < 4:
                    accessible.append((r, c))
        return accessible
    
    total_removed = 0
    
    while True:
        accessible = find_accessible_rolls()
        if not accessible:
            break
        
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    print(total_removed)

if __name__ == "__main__":
    solve()
