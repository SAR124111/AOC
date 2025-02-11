from collections import defaultdict

# Step 1: Open the file in read mode
with open('day11_1.txt', 'r') as file:
    # Step 2: Read the contents of the file
    contents = file.read()

# Step 3: Split the contents into a list of numbers (assuming the numbers are space-separated)
stones = contents.split()

# Optional: Convert the list of strings to a list of integers
stones = [int(stone) for stone in stones]

# Initialize the dictionary with the count of each stone
stone_counts = defaultdict(int)
for stone in stones:
    stone_counts[stone] += 1

def blink(stone_counts):
    new_stone_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == 0:
            new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            # Split the stone into two stones
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stone_counts[left] += count
            new_stone_counts[right] += count
        else:
            new_stone_counts[stone * 2024] += count
    return new_stone_counts

# Example usage
for _ in range(75):  # Blink 75 times
    stone_counts = blink(stone_counts)

# Calculate the total number of stones
total_stones = sum(stone_counts.values())

# Print the total number of stones after 75 blinks
print(total_stones)