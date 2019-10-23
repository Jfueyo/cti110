# This program uses nested loops to draw a pattern
# 16 October 2019
# CTI-110 P4HW3 - Nested Loops
# John Fueyo
#

# Set range of outer loop "step" to iterate 6 times.
# Print # at start each iteration.
# Stay on same line.
# Set range of inner loop "space" to the value of outer loop "step".
# "space" iterates the number of times of the value of "step" loop
# and adds a space on the same line each iteration.
# Print # after "space" completes to complete the outer loop.
# Outer loop "step" begins new iteration on the next line.


# Named constant
HEIGHT = 6

for step in range(HEIGHT):  # Outer loop  
    print('#', end='')
    for space in range (step): # Inner loop
        print(' ', end='')
    print('#')


