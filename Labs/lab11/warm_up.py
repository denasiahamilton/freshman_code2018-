import turtle

def main():
    myt = turtle.Turtle()
    myt.showturtle()
    myt.fillcolor("red")
    myt.begin_fill()
    myt.circle(50)
    myt.pendown()
    myt.end_fill()

    myt.penup()
    myt.goto(-50,-50)
    myt.pendown()
    myt.fillcolor("blue")
    myt.begin_fill()
    for i in range(4):
        myt.forward(100)
        myt.right(90)
    myt.end_fill()

if __name__ == "__main__":
    main()
