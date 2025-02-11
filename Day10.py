def parse_input_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]
    return grid

def find_trailheads(grid):
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def bfs(grid, start):
    from collections import deque
    queue = deque([start])
    visited = set()
    reachable_nines = set()
    
    while queue:
        r, c = queue.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append((nr, nc))
    
    return reachable_nines

def calculate_scores(grid, trailheads):
    total_score = 0
    for trailhead in trailheads:
        reachable_nines = bfs(grid, trailhead)
        total_score += len(reachable_nines)
    return total_score

def main(filename):
    grid = parse_input_from_file(filename)
    trailheads = find_trailheads(grid)
    total_score = calculate_scores(grid, trailheads)
    return total_score

# Example usage
filename = 'Day10.txt'
print(main(filename))