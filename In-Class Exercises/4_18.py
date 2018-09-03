def histo(scorelist):
    d = { }
    for x in scorelist:
        count = scorelist.count(x)
        d[x] = count
    return d

histo([1,4,5,6,7,8])


def isEqual(list1, list2):
    if len(list1) !=  len(list2):
        return False
    elif len(list1) == len(list2):
        if isEqual(list1[1: ]) == isEqual(list2[1: ])

isEqual([1,2,3], [1,2,3])

#private variables
class Time():
    def __init__(self, hours = 0, minutes = 0):
        self.__hours = hours
        self.__minutes = minutes

    def aTuple(self):
        return (hours, minutes)

    def __str__(self):
        return str(self.__hours) + ": " + str(self.__minutes)
         
#Write a short Python code segment that employs a for loop to create a list of 10 Time objects that represent the whole hours from midnight through 9:00am (note that midnight is 00:00). The list should be bound to a variable named tlist. Note: you do not have to write a complete program or function, just the statements necessary to accomplish the task:
tlist  = [ ]
for i in range(10):
    tlist.append(Time(i, 0))
