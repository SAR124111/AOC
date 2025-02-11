# Step 1: Open the file in read mode
with open('day11_1.txt', 'r') as file:
    # Step 2: Read the contents of the file
    contents = file.read()

# Step 3: Split the contents into a list of numbers (assuming the numbers are space-separated)
stones = contents.split()

# Optional: Convert the list of strings to a list of integers
stones = [int(stone) for stone in stones]

# Print the list of stones to verify
print(stones)

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            # Split the stone into two stones
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(stone * 2024)
    return new_stones

# Example usage
for _ in range(25):  # Blink 25 times
    stones = blink(stones)

# Print the final list of stones
print(stones)
# Print the number of stones after 25 blinks
print(len(stones))