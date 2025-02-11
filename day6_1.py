def read_input(file_path):
    # Open the file at the given file path and read its lines
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data


def parse_map(data):
    # Parse the input data into a 2D list (map)
    map_data = []
    for line in data:
        map_data.append(list(line))
    return map_data


def turn_right(direction):
    # Return the new direction when turning right
    directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    return directions[direction]


def move_forward(position, direction):
    # Calculate the new position based on the current direction
    if direction == '^':
        return (position[0] - 1, position[1])
    elif direction == '>':
        return (position[0], position[1] + 1)
    elif direction == 'v':
        return (position[0] + 1, position[1])
    elif direction == '<':
        return (position[0], position[1] - 1)


def simulate_guard_path(map_data):
    # Find the initial guard position and direction
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell in ['^', '>', 'v', '<']:
                guard_position = (i, j)
                guard_direction = cell
                map_data[i][j] = '.'
                break

    visited_positions = set()
    visited_positions.add(guard_position)

    rows = len(map_data)
    cols = len(map_data[0])

    while True:
        next_position = move_forward(guard_position, guard_direction)

        if not (0 <= next_position[0] < rows and 0 <= next_position[1] < cols):
            # End the journey if the guard steps out of the grid
            break

        if map_data[next_position[0]][next_position[1]] == '.':
            guard_position = next_position
            visited_positions.add(guard_position)
        else:
            guard_direction = turn_right(guard_direction)

    return visited_positions


def main():
    # Read the input file
    file_path = 'day6.txt'
    data = read_input(file_path)
    # Parse the input data into a map
    map_data = parse_map(data)

    # Simulate the guard's path and get visited positions
    visited_positions = simulate_guard_path(map_data)

    # Print the number of unique locations visited
    print("Number of unique locations visited:", len(visited_positions))


if __name__ == "__main__":
    main()
