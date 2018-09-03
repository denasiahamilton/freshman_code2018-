
class Complex:
    def __init__(self, x=3, y=1):
        self.__real = x
        self.__imaginary = y

    def getReal(self):
        print (self.__real)

    def getImaginary(self):
        print (self.__imaginary)

    def setReal(self,x):
        self.__real = x

    def setImaginary(self,y):
        self.__real = y

    def __add__(self,other):
        return (self.__real + other.__real, self.__imaginary + other.__imaginary)

    def __sub__(self,other):
        return (Complex(self.__real - other.__real, self.__imaginary - other.__imaginary))

    def __str__(self):
        return (str(self.__real) + "+" + str(self.__imaginary) + "i")
