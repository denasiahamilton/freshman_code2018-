import turtle

def drawSquares():
    turtle.speed(1)
    turtle.showturtle()
    angle = turtle.numinput(" ", "Enter a rotation angle: ")


    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.left(angle)

def main():
    count = 0
    while count < 10:
        drawSquares()
        count = count + 1

if __name__ == '__main__':
    main()
