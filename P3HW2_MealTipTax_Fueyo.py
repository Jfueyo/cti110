# CTI-110
# P3HW2 - MealTipTax
# John Fueyo
# 02 October 2019
#


# Pseudocode (detail algorithm)
# tax = .06
# Input charge for the meal
# Input desired tip percentage (.16 , .18 or .2)
# if tip == .16
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
#   Display original food charge
#   Display tip
#   Display tax
# # Display total cost of meal
# elif tip == .18
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
#   Display original food charge
#   Display tip
#   Display tax
#   Display total cost of meal
# elif tip == .2
#   Set tip = food * tip percent
#   Set tax = food * tax rate
#   Set total meal cost = food + tip + tax
#   Display original food charge
#   Display tip
#   Display tax
#   Display total cost of meal
# else 
#   Display "This is not a valid tip percentage."

taxRate = .06
food = float(input('Enter the cost of your food: '))
tipRate = float(input('Enter a tip of 16%, 18%, or 20% in decimal form: '))

if tipRate == .16:
    
    tip = food * tipRate
    tax = food * taxRate
    totalMeal = food + tip + tax
    print('The original charge for this meal is: $', format(food, ',.2f'), sep='')
    print('The tip for this meal is: $', format(tip, ',.2f'), sep='')
    print('The tax for this meal is: $', format(tax, ',.2f'), sep='')
    print('The total cost of this meal is: $', format(totalMeal, ',.2f'), sep='')

elif tipRate == .18:

    tip = food * tipRate
    tax = food * taxRate
    totalMeal = food + tip + tax
    print('The original charge for this meal is: $', format(food, ',.2f'), sep='')
    print('The tip for this meal is: $', format(tip, ',.2f'), sep='')
    print('The tax for this meal is: $', format(tax, ',.2f'), sep='')
    print('The total cost of this meal is: $', format(totalMeal, ',.2f'), sep='')

elif tipRate == .2: 

    tip = food * tipRate
    tax = food * taxRate
    totalMeal = food + tip + tax
    print('The original charge for this meal is: $', format(food, ',.2f'), sep='')
    print('The tip for this meal is: $', format(tip, ',.2f'), sep='')
    print('The tax for this meal is: $', format(tax, ',.2f'), sep='')
    print('The total cost of this meal is: $', format(totalMeal, ',.2f'), sep='')
    
else:
    print('This is not a valid tip percentage')


