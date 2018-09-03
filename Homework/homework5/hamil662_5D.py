#CSCI 1133 Homework 5
#Denasia Hamilton
#Problem 5D

import turtle
#placement & amount of squares
def squares(t,length,depth):
    if depth == 0: #base case
        return
    else:
        originalSquare(t,length)
        x = length/4
        y = length
        t.goto(x,y) #next origin - top
        squares(t,length/2,depth-1)
        x = length/2
        y = length/4
        t.goto(-x,y) #next origin - left
        squares(t,length/2,depth-1)
        x = length/4
        y = length/2
        t.goto(x,-y) #next origin - bottom
        squares(t,length/2,depth-1)
        x = length
        y = length/4
        t.goto(x,y) #next origin - right
        squares(t,length/2,depth-1)

#function to draw squares
def originalSquare(t,length):
    for i in range(4):
        t.pendown()
        t.forward(length)
        t.left(90)
        t.penup()
        x = t.xcor()
        y = t.xcor()

def main():
    depth = int(input("Enter a depth: "))
    t = turtle.Turtle()
    turtle.speed(0)
    squares(t, 200, depth)

if __name__ == "__main__":
    main()
