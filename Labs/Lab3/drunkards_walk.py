import turtle
import random

def path():
    degree = random.randint(1,4)
    print("The degree is" , degree)
    if degree == 1:
        turtle.left(90)
    elif degree== 2:
        turtle.left(180)
    elif degree == 3:
        turtle.left(270)
    else:
        turtle.left(360)
    turtle.forward(20) #walk 20 steps

def main():
    turtle.speed(0)
    turtle.showturtle()
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.setworldcoordinates(-100,-100,100,100)
    count = 0 #always starts with 0 and use the counter function to add the numbe rof steps moved
    while abs(x) < 100 and abs(y) != 100:
        x = turtle.xcor()
        y = turtle.ycor()
        path()
        count +=20
        print(count)

if __name__ == '__main__':
    main()
