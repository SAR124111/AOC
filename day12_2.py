def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_groups(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    groups = []

    def dfs(r, c, char):
        stack = [(r, c)]
        group = []
        while stack:
            x, y = stack.pop()
            if 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] == char:
                visited[x][y] = True
                group.append((x, y))
                stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
        return group

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                char = grid[r][c]
                group = dfs(r, c, char)
                if group:
                    groups.append((char, group))

    return groups

def calculate_area_perimeter_sides(groups):
    results = []
    for char, group in groups:
        area = len(group)
        perimeter = 0
        sides = set()
        group_set = set(group)
        for x, y in group:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in group_set:
                    perimeter += 1
                    # Add the edge to the sides set
                    if dx != 0:
                        sides.add((min(x, nx), y, max(x, nx), y))
                    if dy != 0:
                        sides.add((x, min(y, ny), x, max(y, ny)))
        results.append((char, area, perimeter, len(sides)))
    return results

def main():
    file_path = 'day12_1.txt'
    grid = read_input(file_path)
    groups = find_groups(grid)
    results = calculate_area_perimeter_sides(groups)

    total_sum = 0
    total_sides = 0
    for char, area, perimeter, sides in results:
        print(f"Character: {char}, Area: {area}, Perimeter: {perimeter}, Sides: {sides}")
        total_sum += area * perimeter
        total_sides += area * sides

    print(f"Total sum of area times perimeter for each region: {total_sum}")
    print(f"Total sum of area times sides for each region: {total_sides}")

if __name__ == '__main__':
    main()