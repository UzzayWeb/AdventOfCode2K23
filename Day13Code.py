import sys
from collections import defaultdict, Counter

# Read the input file specified as a command-line argument and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

# Iterate through two cases: part2=False and part2=True
for part2 in [False, True]:
    ans = 0

    # Split the input data into grids separated by empty lines
    for grid in input_data.split('\n\n'):
        # Create a 2D grid from the current input grid
        G = [[c for c in row] for row in grid.split('\n')]
        R = len(G)
        C = len(G[0])

        # Check for vertical symmetry
        for c in range(C - 1):
            badness = 0
            for dc in range(C):
                left = c - dc
                right = c + 1 + dc
                if 0 <= left < right < C:
                    for r in range(R):
                        if G[r][left] != G[r][right]:
                            badness += 1
            if badness == (1 if part2 else 0):
                ans += c + 1

        # Check for horizontal symmetry
        for r in range(R - 1):
            badness = 0
            for dr in range(R):
                up = r - dr
                down = r + 1 + dr
                if 0 <= up < down < R:
                    for c in range(C):
                        if G[up][c] != G[down][c]:
                            badness += 1
            if badness == (1 if part2 else 0):
                ans += 100 * (r + 1)

    # Print the result for the current case
    print(ans)
