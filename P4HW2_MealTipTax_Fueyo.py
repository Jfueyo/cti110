# CTI-110
# P4HW2 - MealTipTax
# John Fueyo
# 16 October 2019
#


# Pseudocode (detail algorithm)
# tax = 6%
# Input charge for the meal
# Input desired tip percentage (.16 , .18 or .2)
# Test to make sure the inputted tip percentage is .16, .18, or .20
# If not, display "This is not a valid tip percentage"
# Prompt user for a new tip percentage of .16, .18, or .20 until they do so
# if tip == .16
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
# elif tip == .18
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
# else
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
# Display original food charge
# Display tip
# Display tax
# Display total cost of meal
# Ask user if they want to choose another tip percentage (y/n)
# If 'y' then loop back to prompt for new tip percentage and run through loop again.
# If any other value is inputted, exit program.

# Initialized variables
taxRate = .06 
another = 'y'

food = float(input('Enter the cost of your food: '))

# While loop continues as long as user inputs 'y' at end.
while another == 'y': 
    
    print('Enter a tip of 16%, 18%, or 20% (enter .16, .18, or .20): ')
    tipRate = float(input())

    # Tests to see if the inputted tip percentage is .16, .18, or .20
    while tipRate != .16 and tipRate != .18 and tipRate != .20:
        print('This is not a valid tip percentage.')
        tipRate = float(input('Enter a tip of 16%, 18%, or 20% (enter .16, .18, or .20): '))

    # evaluates tipRate at 16%
    if tipRate == .16: 
        tip = food * tipRate
        tax = food * taxRate
        totalMeal = food + tip + tax

    # evaluates tipRate at 18%
    elif tipRate == .18:    
        tip = food * tipRate
        tax = food * taxRate
        totalMeal = food + tip + tax   

    # evaluates tipRate at 20%
    else: 
        tip = food * tipRate
        tax = food * taxRate
        totalMeal = food + tip + tax

    # Display results to user
    print('The original charge for this meal is: $', format(food, ',.2f'), sep='')
    print('The tip for this meal is: $', format(tip, ',.2f'), sep='')
    print('The tax for this meal is: $', format(tax, ',.2f'), sep='')
    print('The total cost of this meal is: $', format(totalMeal, ',.2f'), sep='')

    # Prompt user if they want to choose another tip percentage.
    # Begins loop over if true
    another = input("Do you want to choose another tip of 16%, 18%, or 20% instead (enter .16, .18, or .20)? (y/n): ")

        


    






