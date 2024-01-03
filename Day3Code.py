import sys
from collections import defaultdict

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()
lines = input_data.split('\n')

# Create a 2D grid from the input data
grid = [[char for char in line] for line in lines]
rows = len(grid)
columns = len(grid[0])

# Initialize player scores
player1_score = 0
gear_values = defaultdict(list)

# Iterate through the grid rows and columns
for row in range(rows):
    gear_positions = set()  # Store positions of '*' characters next to numbers
    current_number = 0
    has_component = False

    # Iterate through characters in the current row
    for col in range(len(grid[row]) + 1):
        if col < columns and grid[row][col].isdigit():
            current_number = current_number * 10 + int(grid[row][col])

            # Check neighboring positions for '*' characters
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row + dr < rows and 0 <= col + dc < columns:
                        neighbor_char = grid[row + dr][col + dc]
                        if not neighbor_char.isdigit() and neighbor_char != '.':
                            has_component = True
                        if neighbor_char == '*':
                            gear_positions.add((row + dr, col + dc))
        elif current_number > 0:
            for gear_position in gear_positions:
                gear_values[gear_position].append(current_number)
            if has_component:
                player1_score += current_number
            current_number = 0
            has_component = False
            gear_positions = set()

# Print player 1's score
print("Player 1 Score:", player1_score)

# Calculate player 2's score based on gear positions
player2_score = 0
for position, values in gear_values.items():
    if len(values) == 2:
        player2_score += values[0] * values[1]

# Print player 2's score
print("Player 2 Score:", player2_score)
