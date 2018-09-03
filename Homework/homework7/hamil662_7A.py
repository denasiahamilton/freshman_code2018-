#CSCI 1133 Homework 7
#Denasia Hamilton
#Problem 7A


class Complex():
    def __init__(self, real = 0.0, imaginary = 0.0):
        self.__real = real
        self.__imaginary = imaginary

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
        if self.__imaginary < 0:
            return str(float(self.__real)) + str(float(self.__imaginary)) + "i"
        if self.__real == 0:
            return float(self.__imaginary)
        if self.__imaginary == 0:
            return float(self.__real)
        if self.__real == 0 and self.__imaginary == 0:
            return int(0)

def main():
    real1 = input("Enter the real part of the first complex number: ")
    imaginary1 = input("Enter the imaginary part of the first complex number: ")
    real2 = input("Enter the real part of the second complex number: ")
    imaginary2 = input("Enter the imaginary part of the second complex number: ")

    C1 = Complex(int(real1), int(imaginary1))
    C2 = Complex(int(real2),int(imaginary2))

    print("C1 =", C1)
    print("C2 =", C2)
    print("C1+C2 =", C1 + C2)
    print("C1-C2 =", C1 - C2)
    print("C1*C2 =", C1 * C2)
    print("C1/C2 =", C1 / C2)

if __name__ == '__main__':
    main()
