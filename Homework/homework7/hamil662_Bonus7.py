#CSCI 1133 Homework 6
#Denasia Hamilton
#Problem -- Bonus

import turtle

class Complex():
    def __init__(self, real = 0.0, imaginary = 0.0, color = "black"):
        self.__real = real
        self.__imaginary = imaginary
        self.__color = color

    def __add__(self,rhand):
        return Complex(self.__real + rhand.__real, self.__imaginary + rhand.__imaginary)

    def __sub__(self,rhand):
        return Complex(self.__real - rhand.__real, self.__imaginary - rhand.__imaginary)

    def __mul__(self,rhand):
        return Complex(self.__real * rhand.__real - self.__imaginary * rhand.__imaginary, self.__real * rhand.__imaginary + self.__imaginary * rhand.__real)

    def __truediv__(self,rhand):
        if rhand.__real == 0 and rhand.__imaginary == 0:
            return "None; Divide by Zero Error!"
        else:
            return Complex((self.__real * rhand.__real + self.__imaginary * rhand.__imaginary)/(rhand.__real ** 2 + rhand.__imaginary ** 2), (self.__imaginary * rhand.__real - self.__real * rhand.__imaginary)/(rhand.__real ** 2 + rhand.__imaginary **2 ))

    def __str__(self):
        if self.__real and self.__imaginary > 0:
            return str(float(self.__real)) + "+" + str(float(self.__imaginary)) + "i"
        elif self.__imaginary < 0:
            return str(float(self.__real)) + str(float(self.__imaginary)) + "i"
        elif self.__real == 0:
            return str(float(self.__imaginary))
        elif self.__imaginary == 0:
            return str(float(self.__real))
        elif self.__real == 0 and self.__imaginary == 0:
            return int(0)

    def plot(self):
        self.t = turtle.Turtle()
        self.t.color(self.__color)
        self.t.write(C,font=("Ariel", 10, "normal"))
        self.t.dot(self.__color)


def makeGraph(fnameCVS):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-250,0)
    t.pendown()
    t.forward(500)
    t.write("r",True, align = "center", font=("Ariel", 10, "normal"))
    t.penup()
    t.goto(0,-250)
    t.left(90)
    t.pendown()
    t.forward(500)
    t.write("i",True, align = "center", font=("Ariel", 10, "normal"))

    text_file = open(fnameCVS, "r")
    reading_file = text_file.readline()
    plotting = [ ]

    while True:
        thisLine = text_file.readline()
        if len(thisLine) == 0:
            break
        parsing = thisLine.strip()
        parsing = parsing.split(",")

        for x in parsing:
            if x in parsing[0]:
                real = x
                x_cord = int(real)

            if x in parsing[1]:
                imaginary = x
                y_cord = int(imaginary)

            if x in parsing[2]:
                color = x

                C = Complex(int(real), int(imaginary), color)

        t.goto(x_cord, y_cord)
        t.color(color)
        t.write(C,font=("Ariel", 10, "normal"))
        t.dot(color)
        t.penup()

    text_file.close()
makeGraph("complexList.csv")
