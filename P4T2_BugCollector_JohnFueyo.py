# This program keeps the running total of bugs collected during 7 days.
# 15 October 2019
# CTI-110 P4T2 - Bug Collector
# John Fueyo
#

# Set total = 0
# for each of 7 days:
#   Input bugs collected for a day
#   Add bugs collected to total
# Display total

#Initialize the accumulator
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)
    # Input the number of bugs.
    bugs = int(input())
    # Add bugs to total
    total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
