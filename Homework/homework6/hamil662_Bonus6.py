#CSCI 1133 Homework 6
#Denasia Hamilton
#Problem -- Bonus

import turtle

class Insect:
    def __init__(self, pair_of_legs = 4, legs_color = "purple", body_size = 50):
        self.pair_of_legs = pair_of_legs
        self.legs_color = legs_color
        self.body_size = body_size
        self.t = turtle.Turtle()
        self.t.speed(0)

    def draw_legs(self):
        self.t.penup()
        y = -150
        for i in range(self.pair_of_legs):
            self.t.goto(50,y)
            self.t.pendown()
            self.t.color(self.legs_color)
            self.t.forward(60)
            self.t.right(60)
            self.t.forward(60)
            self.t.left(60)
            self.t.penup()
            self.t.goto(0,y)
            self.t.goto(-50,y)
            self.t.pendown()
            self.t.forward(-60)
            self.t.left(240)
            self.t.forward(60)
            self.t.penup()
            self.t.right(240)
            y += 50
        self.t.hideturtle()

class Caterpillar(Insect):
    def __init__(self, body_color = "green"):
        Insect.__init__(self, pair_of_legs = 4, legs_color = "purple", body_size = 50)
        self.body_color = body_color
        self.t = turtle.Turtle()
        self.t.speed(0)

    def draw_body(self):
        self.t.penup()
        y = -200
        self.t.goto(0,y)
        for i in range(5):
            self.t.fillcolor(self.body_color)
            self.t.begin_fill()
            self.t.circle(self.body_size)
            self.t.end_fill()
            y += 50
            self.t.goto(0,y)

    #function for drawing antennae
    def draw_antennae(self):
        self.t.penup()
        self.t.goto(25, 90)
        self.t.left(60)
        self.t.pendown()
        self.t.color(self.legs_color)
        self.t.forward(50)
        self.t.penup()
        self.t.goto(-25,90)
        self.t.left(60)
        self.t.pendown()
        self.t.forward(50)
        self.t.right(120)

    def display(self):
        self.draw_body()
        self.draw_antennae()
        self.draw_legs()

class LadyBug(Insect):
    def __init__(self, body_color = "black", wing_color = "red"):
        Insect.__init__(self, pair_of_legs = 4, legs_color = "purple", body_size = 50)
        self.body_color = body_color
        self.wing_color = wing_color
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    #function for drawing body
    def draw_body(self):
        self.t.penup()
        self.t.color(self.body_color)
        self.t.begin_fill()
        self.t.circle(self.body_size)
        self.t.end_fill()
        self.t.goto(0, -190)
        self.t.begin_fill()
        self.t.circle(self.body_size * 2.25)
        self.t.end_fill()

    #function for drawing antennae
    def draw_antennae(self):
        self.t.goto(25,90)
        self.t.pendown()
        self.t.color(self.legs_color)
        self.t.left(60)
        self.t.forward(50)
        self.t.penup()
        self.t.goto(-25,90)
        self.t.left(60)
        self.t.pendown()
        self.t.forward(50)
        self.t.right(120)

    #function for drawing red wings + spots
    def draw_wings(self):
        self.t.penup()
        self.t.goto(35,50)
        self.t.left(170)
        self.t.color(self.wing_color)
        self.t.begin_fill()
        self.t.circle(130,180)
        self.t.end_fill()
        self.t.goto(40,-200)
        self.t.left(390)
        self.t.begin_fill()
        self.t.circle(130,180)
        self.t.end_fill()
        #spots!!!
        self.t.penup()
        self.t.begin_fill()
        self.t.goto(-10,5)
        self.t.color(self.body_color)
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(-60,-120)
        self.t.pendown()
        self.t.begin_fill()
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(70,-100)
        self.t.begin_fill()
        self.t.pendown()
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.begin_fill()
        self.t.goto(10,70)
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.begin_fill()
        self.t.goto(70,0)
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.begin_fill()
        self.t.goto(-80,-30)
        self.t.circle(30)
        self.t.end_fill()
        self.t.penup()
        self.t.begin_fill()
        self.t.goto(-30,70)
        self.t.circle(30)
        self.t.end_fill()

    def display(self):
        self.draw_body()
        self.draw_antennae()
        self.draw_legs()
        self.draw_wings()

class Spider(Insect):
    def __init__(self, body_color = "black"):
        Insect.__init__(self, pair_of_legs = 4, legs_color = "purple", body_size = 50)
        self.body_color = body_color
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    #function for drawing body
    def draw_body(self):
        self.t.penup()
        self.t.color(self.body_color)
        self.t.goto(0,0)
        self.t.begin_fill()
        self.t.circle(self.body_size)
        self.t.end_fill()
        self.t.goto(0, -170)
        self.t.begin_fill()
        self.t.circle(self.body_size * 2)
        self.t.end_fill()

    #function for display
    def display(self):
        self.draw_legs()
        self.draw_body()
