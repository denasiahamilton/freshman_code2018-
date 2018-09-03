#CSCI 1133 Homework1
#Denasia Hamilton
#Problem 1C

import turtle
import math

def shapes(wid, hi):
    width = turtle.numinput(" ", "Enter a width: ")
    height = turtle.numinput(" ", "Enter a height: ")
    hypotenuse = math.hypot(width, height) #triangle, hypotenuse math function
    print ("Hypotenuse length of Right Triangle: ", hypotenuse)
    angle1 = (90 - (math.degrees(math.atan(width/height))))
    angle2 = (180 - (90 - angle1))
    turtle.speed(1)
    turtle.showturtle()
    turtle.left(90)
    turtle.forward(height) #height
    turtle.right(90)
    turtle.forward(width) #width
    turtle.right(90)
    turtle.forward(height) #height
    turtle.goto(0,0) #back to origin
    turtle.left(90)
    turtle.forward(width) #width
    turtle.forward(width) #width
    turtle.left(angle1)
    turtle.forward(hypotenuse) #hypotenuse
    turtle.right(angle2)
    turtle.forward(height) #height
    turtle.right(90)
    turtle.forward(width) #width
    turtle.goto(0,0) #back to origin

shapes("wid", "hi")
