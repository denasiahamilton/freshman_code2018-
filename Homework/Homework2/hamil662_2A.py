#CSCI 1133 Homework2
#Denasia Hamilton
#Problem 2A

first = int(input("Enter the first term of the series: "))
second = int(input("Enter the second term of the series: "))
term = int(input("Enter the number of terms you want to see: "))

def newFib(first, second, term):
    count = 0
    string = str(first) + " " + str(second) + " "
    while count in range(term - 2):
        count += 1
        terms = first + second
        string = string + str(terms) + " "
        first = second
        second = terms
    print ("The first", term, "terms of the new series are: ")
    return string

print(newFib(first, second, term))
