import sys
from collections import defaultdict, Counter

# Read the input file specified as a command-line argument and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

# Create a 2D grid 'G' from the input data
G = [[c for c in row] for row in lines]

# Define a function 'f' to calculate a hash value for a string
def f(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h

# Split the input data into commands separated by commas
cmds = input_data.split(',')

# Part 1: Calculate the sum of hash values for all commands
p1 = 0
for cmd in cmds:
    p1 += f(cmd)
print(p1)

# Initialize a list 'BOX' with 256 empty lists
BOX = [[] for _ in range(256)]

# Process commands to update the BOX data structure
for cmd in cmds:
    if cmd[-1] == '-':
        # Remove an entry from BOX based on the name
        name = cmd[:-1]
        h = f(name)
        BOX[h] = [(n, v) for (n, v) in BOX[h] if n != name]
    elif cmd[-2] == '=':
        # Update or add an entry in BOX with a specified length
        name = cmd[:-2]
        h = f(name)
        len_ = int(cmd[-1])
        if name in [n for (n, v) in BOX[h]]:
            BOX[h] = [(n, len_ if name == n else v) for (n, v) in BOX[h]]
        else:
            BOX[h].append((name, len_))

# Part 2: Calculate the weighted sum of entries in BOX
p2 = 0
for i, box in enumerate(BOX):
    for j, (n, v) in enumerate(box):
        p2 += (i + 1) * (j + 1) * v
print(p2)
