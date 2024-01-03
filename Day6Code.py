import sys
from collections import defaultdict

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()

# Split the input data into lines
lines = input_data.split('\n')

ans = 0 

# Split the lines into time and distance data
time_data, dist_data = lines

# Parse the time and distance values from the input
times = [int(x) for x in time_data.split(':')[1].split()]
dist = [int(x) for x in dist_data.split(':')[1].split()]

# Initialize variables to store concatenated time and distance values
T = ''
for t in times:
    T += str(t)
T = int(T)

D = ''
for d in dist:
    D += str(d)
D = int(D)

# Define a function to calculate the number of occurrences where dx > d
def count_dx_greater_than_d(t, d):
    ans = 0
    for x in range(t + 1):
        dx = x * (t - x)
        if dx > d:
            ans += 1
    return ans

# Initialize the final result
ans = 1

# Calculate the result by multiplying the counts for each time and distance pair
for i in range(len(times)):
    ans *= count_dx_greater_than_d(times[i], dist[i])

# Print the final result
print("Result:", ans)

# Calculate and print the result for the concatenated T and D values
print("Result for T and D:", count_dx_greater_than_d(T, D))
