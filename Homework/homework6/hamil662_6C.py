#CSCI 1133 Homework 6
#Denasia Hamilton
#Problem 6C

import turtle

class Caterpillar:
    def __init__ (self, body_color = "green", legs_color = "purple", body_size = 50):
        self.body_color = body_color
        self.legs_color = legs_color
        self.body_size = body_size
        self.t = turtle.Turtle()
        self.t.speed(0)

    #function for drawing body
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

    #function for drawing legs
    def draw_legs(self):
        self.t.penup()
        y = -150
        for i in range(4):
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
            
    #function for display
    def display(self):
        self.draw_body()
        self.draw_antennae()
        self.draw_legs()
