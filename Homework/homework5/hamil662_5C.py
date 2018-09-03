#CSCI 1133 Homework 5
#Denasia Hamilton
#Problem 5C

def factorials(number_of_terms):
    #base case, can't have negative number_of_terms, and number_of_terms must atleast = 1
    if number_of_terms < 1:
        return 1
    #want to multiply number_of_terms by everything between it and 0
    #w/ if statement, once number_of_terms = 1, it will return 1 and stop factorials recursive call
    else:
        return number_of_terms * factorials(number_of_terms - 1) #recursive call


def taylor(angle, number_of_terms):
    #base case, stopping condition, keep subtracting 1 until number_of_terms < 1, return number_of_terms
    if number_of_terms < 1:
        return number_of_terms

    #use taylor series equation, return for sine value
    else:
        element = taylor(angle, number_of_terms - 1)
        x = ((-1) ** ( number_of_terms - 1) / factorials(2 * number_of_terms - 1))
        return x * (angle ** (2 * number_of_terms - 1)) + element


def main():
    angle = float(input("Enter the angle to approximate (in radians): "))
    number_of_terms = int(input("Enter the number of terms to compute: "))
    print("sin(", float(angle), ") is approximately", taylor(angle,number_of_terms))

if __name__ == "__main__":
    main()
