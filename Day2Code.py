import sys
from collections import defaultdict

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0

# Iterate through each line in the input data
for line in input_data.split('\n'):
    ok = True

    # Split the line into an ID and the events
    id_, line = line.split(':')
    V = defaultdict(int)

    # Split events by semicolon
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)

            # Update the maximum count of each color
            V[color] = max(V[color], n)

            # Check if the count exceeds the specified limits
            if n > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                ok = False

    # Calculate the score for player 2
    score = 1
    for v in V.values():
        score *= v
    p2 += score

    # Check if 'ok' is True and add to player 1 score accordingly
    if ok:
        p1 += int(id_.split()[-1])

# Print the results
print(p1)
print(p2)
