# This program uses the Turtle module to draw repeating squares
# 17 October 2019
# CTI-110 P4T1a - Shapes
# John Fueyo

# Import turtle
# Outer loop "count" iterates 100 times
    # Inner loop "square" makes a square
# After "square" exits, complete outer loop "count"
# Store turtle (x-cord - 3). in var. "x" to move turtle
# left by 3
# Store turtle y-cord. in var. "y"
# Add 3 to var. squareSide to make next square made larger
# Pen goes up
# Turtle goes to (x, y) coordinates stored in variables "x" and "y"
# Pen goes down
# Begin new iteration of loop "count"


#Named constants
NUM_SQUARES = 100
OFFSET = 3

#Variables
squareSide = 5
x = 0
y = 0


import turtle
turtle.showturtle()
turtle.pensize(1)
turtle.speed(0)

for count in range(NUM_SQUARES):
    for square in range(4):
        turtle.forward(squareSide)
        turtle.left(90)
        
    x = turtle.xcor() - OFFSET
    y = turtle.ycor() 

    squareSide = squareSide + OFFSET
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.hideturtle()
turtle.done()
