import re

# Example string
#text = "Here are some examples: mul(12,34), mul(123,456), mul(7,89), and mul(123,567)."

file_path = 'Day3.txt'  # Update the file path here
with open(file_path, 'r') as file:
    text = file.read()

# Define the regex pattern
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches
matches = re.findall(pattern, text)

total = 0
# Process each match
for match in matches:
    x, y = map(int, match)  # Convert the matched strings to integers
    result = x * y  # Multiply the two integers
    total += result

print(total)