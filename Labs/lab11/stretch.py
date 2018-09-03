from turtle import Turtle

class Shape:
    def __init__(self, x = 0, y = 0, the_color = "blue", fill = False):
        #turtle.showturtle()
        self.location = (x,y)
        self.color = the_color
        self.fill = fill

#class Circle:
    #def __init__(radius = 1, shape):

p = Shape(4,5)
the_color = Shape("red")
fill = Shape(True)

print(p.location)
print(the_color.color)
print(fill.fill)
