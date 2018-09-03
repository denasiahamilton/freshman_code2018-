#CSCI 1133 Homework 5
#Denasia Hamilton
#Problem 5A

def flattenList(aList):
    #basecase
    if len(aList) == 0:
        return aList

    #if element is in a list, flatten the element and then the rest of the list
    elif type(aList[0]) == type([]):
        return flattenList(aList[0]) + flattenList(aList[1:])

    #else, return the element, then flatten the rest of the list
    else:
        return [aList[0]] + flattenList(aList[1:])

flattenList([[[[[1]],[6,8],[],4],2,5,[3]]])
