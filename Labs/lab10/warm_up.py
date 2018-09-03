class rational:
    def __init__(self, num=0, den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self, num=0 , den=0):
        if den == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + '/' + str(self.denominator)

num1 = rational(3,1)
num2 = rational(1,3)

print(num1)
