import sys

# Read the input file and strip whitespace
input_data = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0

# Split the input data by newline character
for line in input_data.split('\n'):
    p1_digits = []
    p2_digits = []
    
    # Iterate through each character in the line
    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            # Check if the current substring starts with a number word
            if line[i:].startswith(val):
                p2_digits.append(str(d+1))
    
    # Calculate the sums for player 1 and player 2
    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])

# Print the results
print(p1)
print(p2)
