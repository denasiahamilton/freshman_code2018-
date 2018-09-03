#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 4A

def two_sums(aList, target):
    #if target is string or float, print error
    if type(target) != int:
        print("Error: target", target, "is not an integer")
        return target

    #if there is a string or float in aList, print error
    for x in aList:
        if type(x) != int:
            print("Error:", x, "in list is not an integer")
            return aList

    #check first number through whole list, and then move to the second, and third, etc
    isValid = True
    while isValid:
        for (i,v) in enumerate(aList):
            i = 0
            the_sum = 0
            the_sum = v + aList[i]

            if the_sum == target:
                isValid = False
                print (aList[i], v)

        if the_sum != target:
            del aList[i]

two_sums([3,-1,4,6,7,1], 10)
