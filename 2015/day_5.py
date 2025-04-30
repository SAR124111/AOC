with open("day_5.txt", "r") as file:
    lines = [line.strip() for line in file]

nice_count = 0

for line in lines:
    vowels = "aeiou"
    bad_strings = ["ab", "cd", "pq", "xy"]

    # Condition 1: At least three vowels
    vowel_count = sum(1 for char in line if char in vowels)

    # Condition 2: At least one letter that appears twice in a row
    has_double = any(line[i] == line[i+1] for i in range(len(line)-1))

    # Condition 3: Does not contain bad substrings
    has_bad = any(bad in line for bad in bad_strings)

    if vowel_count >= 3 and has_double and not has_bad:
        nice_count += 1

print(nice_count)
