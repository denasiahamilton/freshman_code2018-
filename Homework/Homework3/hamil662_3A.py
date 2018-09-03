#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 3A


def intvert(a_list):
    #new list for items that have been reversed from input list a_list
    new_list = [ ]
    for (i, v) in enumerate(a_list):
        #increase the index by 1, (ex. the last item (1) is now at index 4)
        i += 1
        #starts at index 4 and adds to new_list from a_list (adds 1 to new_list first)
        new_list.append(a_list[-i])
        for x in new_list:
            #if x item in new_list is a string, remove from new_list
            if type(x) == str:
                new_list.remove(x)
            #and if x item in new_list is a float, remove from new_list
            elif type(x) == float:
                new_list.remove(x)
    #print remaining items, or an empty list
    print(new_list)
intvert([5, "pineapple", 50.5, 1])

"""
Additional Inputs tested and output:
    example 1: intvert([34, "asjadfadfaosdf", 15.5, "integer", -3])
    output: [-3, 34]

    example 2: intvert([1234, 0.0, [1,2,3,4,5], "denasia", 54,[], 3])
    output: [3, [], 54, [1, 2, 3, 4, 5], 1234]
"""
