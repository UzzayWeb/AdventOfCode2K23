import sys
from collections import defaultdict

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()
lines = input_data.split('\n')

# Initialize player 1's score and a dictionary to track counts
player1_score = 0
line_counts = defaultdict(int)

# Iterate through lines with enumeration
for i, line in enumerate(lines):
    line_counts[i] += 1
    first_part, rest_part = line.split('|')
    id_, card_part = first_part.split(':')

    # Parse card and rest as lists of integers
    card_nums = [int(x) for x in card_part.split()]
    rest_nums = [int(x) for x in rest_part.split()]

    # Calculate the number of common elements between card and rest
    common_elements = len(set(card_nums) & set(rest_nums))

    if common_elements > 0:
        player1_score += 2**(common_elements - 1)

    # Update counts for lines that depend on the current line
    for j in range(common_elements):
        line_counts[i + 1 + j] += line_counts[i]

# Print player 1's score
print("Player 1 Score:", player1_score)

# Calculate the total count of lines
total_line_count = sum(line_counts.values())

# Print the total line count
print("Total Line Count:", total_line_count)
