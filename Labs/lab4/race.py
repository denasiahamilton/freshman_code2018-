import turtle
import random

def race():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()

    turtle.showturtle()
    turtle.speed(3)
    turtle.setworldcoordinates(-500,-500,500,500)

    turtle.penup()
    t1.goto(-100,0)
    t1.shape("turtle")
    t1.color("red")

    turtle.penup()
    t2.goto(-100, 50)
    t2.shape("turtle")
    t2.color("blue")

    turtle.penup()
    t3.goto(-100, -50)
    t3.shape("turtle")
    t3.color("green")

    move = random.randint(1,15)
    print ("The number of steps is", move)
    t1.forward(move)
    t2.forward(move)
    t3.forward(move)

race()
