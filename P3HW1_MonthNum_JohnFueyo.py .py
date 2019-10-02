# CTI-110
# P3HW1 - Month number
# John Fueyo
# 02 October 2019
#

# Pseudocode comment block
# Input the months number
# If number is less than 1 or greater than 12, display error.
# elif month == 1/2/3/4/5/6/7/8/9/10/11
#   Display Jan/Feb/Mar/Apr/May/June/July/Aug/Sept/Oct/Nov.
# else
#   Display Dec.

month = int(input("Enter a months number from 1-12: "))

if month < 1 or month > 12:
    print("That number is not between 1 and 12")           
elif month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
else: 
    print("December")
