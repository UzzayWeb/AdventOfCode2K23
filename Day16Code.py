import sys
from collections import defaultdict, Counter

# Read the input file specified as a command-line argument and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

# Create a 2D grid 'G' from the input data
G = [[c for c in row] for row in lines]

# Get the dimensions of the grid
R = len(G)
C = len(G[0])

# Define possible movements: up, right, down, left
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

# Define a function 'step' to move in a specific direction
def step(r, c, d):
    return (r + DR[d], c + DC[d], d)

# Define a function 'score' to calculate the score starting from a specific position and direction
def score(sr, sc, sd):
    POS = [(sr, sc, sd)]  # Initialize the position list with the starting position
    SEEN = set()         # Set to store visited positions
    SEEN2 = set()        # Set to store visited positions with direction
    while True:
        NP = []  # Next positions to explore
        if not POS:
            break  # Exit if there are no more positions to explore
        for (r, c, d) in POS:
            if 0 <= r < R and 0 <= c < C:
                SEEN.add((r, c))  # Mark the position as visited
                if (r, c, d) in SEEN2:
                    continue  # Skip if the position with direction has been visited
                SEEN2.add((r, c, d))  # Mark the position with direction as visited
                ch = G[r][c]  # Get the character at the current position
                if ch == '.':
                    NP.append(step(r, c, d))  # Move in the current direction
                elif ch == '/':
                    NP.append(step(r, c, {0: 1, 1: 0, 2: 3, 3: 2}[d]))  # Turn right
                elif ch == '\\':
                    NP.append(step(r, c, {0: 3, 1: 2, 2: 1, 3: 0}[d]))  # Turn left
                elif ch == '|':
                    if d in [0, 2]:
                        NP.append(step(r, c, d))  # Continue in the current direction
                    else:
                        NP.append(step(r, c, 0))  # Move up
                        NP.append(step(r, c, 2))  # Move down
                elif ch == '-':
                    if d in [1, 3]:
                        NP.append(step(r, c, d))  # Continue in the current direction
                    else:
                        NP.append(step(r, c, 1))  # Move right
                        NP.append(step(r, c, 3))  # Move left
                else:
                    assert False  # Handle unexpected characters
        POS = NP  # Update the positions to explore
    return len(SEEN)  # Return the number of visited positions

# Calculate the score starting from position (0, 0) with direction 1
print(score(0, 0, 1))

# Initialize the maximum score 'ans' to 0
ans = 0

# Iterate over rows and columns to find the maximum score
for r in range(R):
    ans = max(ans, score(r, 0, 1))  # Start from the left side
    ans = max(ans, score(r, C-1, 3))  # Start from the right side
for c in range(C):
    ans = max(ans, score(0, c, 2))  # Start from the top
    ans = max(ans, score(R-1, c, 0))  # Start from the bottom

# Print the maximum score
print(ans)
