class measure:
    def __init__(self, ft = 0, inx=0):
        if inx > 12:
            new_inches = inx - 12
            ft += 1
            inx = new_inches
            self.inches = inx
        self.feet = ft

    def __add__(self):

    def __sub__(self):


    def __str__(self):
        return str(self.feet) + ' feet ' + str(self.inches) + ' inches '

num0 = measure()
num1 = measure(4,15)
num2 = measure(48)

print(num1)
