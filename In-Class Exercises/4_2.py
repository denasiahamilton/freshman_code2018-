import turtle

class TurtleGTX(turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.odometer = 0

    def forward(self,n):
        if (n>0):
            turtle.forward(self,n)
            self.odometer += n
        else:
            turtle.forward(self,n)
            self.odometer -= n
