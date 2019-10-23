# This program uses the Turtle module to draw the initials "JF"
# 17 October 2019
# CTI-110 P4T1b - Initials
# John Fueyo


# Import turtle
# Draw semi-circle
# Draw up to reach intersection of horizontal and vertical part of "J"
# Turtle left 90
# 180 degree direction change
# Turtle forward to complte horizontal part of "J"
# Pen up
# Enter new (x, y) coordinate to begin "F"
# Pen down
# Draw horizontal part of "F"
# 180 degree turn
# Forward to intersection of top horizontal and vertical parts of "F"
# 90 degree turn left
# forward to bottom of vertical part of "F"
# 180 degree turn
# Forward to central intersection of vertical and horizontal parts of "F"
# 90 degrees right
# Forward to complete central horizontal piece
# Hide turtle

import turtle
turtle.showturtle()
turtle.pensize(8)
turtle.speed(0)
turtle.pencolor("green")

turtle.right(90)
turtle.circle(25,180)
turtle.forward(60)
turtle.left(90)
turtle.forward(35)
turtle.left(180)
turtle.forward(70)

turtle.penup()
turtle.goto(100, 60)
turtle.pendown()

turtle.forward(70)
turtle.left(180)
turtle.forward(70)
turtle.left(90)
turtle.forward(85)
turtle.left(180)
turtle.forward(42.5)
turtle.right(90)
turtle.forward(40)

turtle.hideturtle()
turtle.done()
