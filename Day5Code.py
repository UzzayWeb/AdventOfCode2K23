import sys
from collections import defaultdict

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

# Split the input data into parts
parts = input_data.split('\n\n')

# Extract the seed and convert it into a list of integers
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

# Define a class for a Function
class Function:
    def __init__(self, S):
        # Split the string into lines and discard the first line (name)
        lines = S.split('\n')[1:]

        # Initialize tuples to store dst, src, sz values
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def apply_one(self, x: int) -> int:
        # Apply a single transformation to x based on the tuples
        for (dst, src, sz) in self.tuples:
            if src <= x < src + sz:
                return x + dst - src
        return x

    def apply_range(self, R):
        A = []
        for (dest, src, sz) in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R

# Create a list of Function objects from the input
Fs = [Function(s) for s in others]

P1 = []
for x in seed:
    for f in Fs:
        x = f.apply_one(x)
    P1.append(x)

# Print the minimum value of P1
print("Minimum P1:", min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
    R = [(st, st + sz)]
    for f in Fs:
        R = f.apply_range(R)
    P2.append(min(R)[0])

# Print the minimum value of P2
print("Minimum P2:", min(P2))
