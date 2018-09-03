import turtle
import math
def olympic():
    radius = int(input("Enter a number: ")) #radius has to be over 50 
    turtle.speed(2)
    turtle.showturtle()
    turtle.pensize(5)
    turtle.color("blue")
    turtle.circle(radius)

    turtle.color("yellow")
    turtle.penup()
    turtle.goto(50, -50)
    turtle.pendown()
    turtle.circle(radius)

    turtle.color("black")
    turtle.penup()
    turtle.goto(110,0)
    turtle.pendown()
    turtle.circle(radius)

    turtle.color("green")
    turtle.penup()
    turtle.goto(180,-50)
    turtle.pendown()
    turtle.circle(radius)

    turtle.color("red")
    turtle.penup()
    turtle.goto(220,0)
    turtle.pendown()
    turtle.circle(radius)

olympic()
