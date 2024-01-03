import sys
from math import gcd
from collections import defaultdict, Counter

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

# Define a function 'f' to calculate the result recursively
def f(xs, part2):
    # Base case: if all elements in 'xs' are 0, return 0
    if all(x == 0 for x in xs):
        return 0
    
    D = []
    
    # Calculate the differences between adjacent elements in 'xs'
    for i in range(len(xs) - 1):
        D.append(xs[i + 1] - xs[i])
    
    # Recursively calculate the result
    return xs[0 if part2 else -1] + (-1 if part2 else 1) * f(D, part2)

# Iterate through two cases: part2=False and part2=True
for part2 in [False, True]:
    ans = 0
    
    # Iterate through lines in the input data
    for line in lines:
        xs = [int(x) for x in line.split()]
        ans += f(xs, part2)
    
    # Print the result for the current case
    print(ans)
