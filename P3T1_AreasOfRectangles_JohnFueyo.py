# This program calculates the area of two rectangles
# and prints which one is greater or if they have equal areas.
# CTI-110
# P3T1- Areas of Rectangles
# John Fueyo
# 02 October 2019
#

# Input the length and width of rectangle1
# Input the length and width of rectangle2
# Calculate the area of rectangle1
# Calculate the area of rectangle2
# Compare rectangle1 to rectangle2
# if area1 > area2
#   Display "rectangle1 has the greatest area."
# else if area2 > area 1
#   Display "rectangle2 has the greatest area."
# else
#   Display "Both rectangles have the same area."

# Get dimensions of rectangle1
length1 = int(input("Enter the length of rectangle 1: "))
width1 = int(input("Enter the width of rectangle 1: "))

# Get dimensions of rectangle2
length2 = int(input("Enter the length of rectangle 2: "))
width2 = int(input("Enter the width of rectangle 2: "))

# Calculate the area of the rectangles
area1 = length1 * width1
area2 = length2 * width2

# Determine which has the greater area
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("Both rectangles have the same area.")
