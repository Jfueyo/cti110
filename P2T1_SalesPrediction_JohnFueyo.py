# This program takes input of total sales and displays the profit
# 22 September 2019
# CTI-110 P2T1 - Sales Prediction
# John Fueyo
#

# Get the projected total sales.
totalSales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = totalSales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
