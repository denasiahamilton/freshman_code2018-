#CSCI 1133 Homework2
#Denasia Hamilton
#Problem 2C

import turtle

def drawTri(size): #draw a triangle given size
    turtle.showturtle()
    turtle.speed(3)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.goto(0,0)

def drawSqr(size): #draw a square given size
    turtle.showturtle()
    turtle.speed(3)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.goto(0,0)

def drawOct(size): #draw an octogon given size
    turtle.showturtle()
    turtle.speed(3)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.forward(size)
    turtle.left(45)
    turtle.goto(0,0)

def main():
    shape = input("What kind of shape do you want to draw? ")
    shape = shape.lower()
    while shape != "triangle" and shape!= "octogon" and shape != "square": #prompt user to put valid shape
        print("ERROR:", shape, "is not a valid choice. Please enter triangle, square, or octogon!")
        shape = input("What kind of shape do you want to draw? ")
        shape = shape.lower() #not case-sensitive
    amount = int(input("How many would you like to draw? "))
    size = int(input("How big should the shapes be? "))
    count = 0
    while count < amount:
        count = count + 1
        if shape == "triangle":
            drawTri(size)
        elif shape == "square":
            drawSqr(size)
        else:
            drawOct(size)
        angle = 360 / amount
        turtle.left(angle)

if __name__ == '__main__':
    main()
