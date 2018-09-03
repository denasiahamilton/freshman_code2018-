#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 4C

def merge2(sentence1, sentence2):
    #split each sentence and place them in a list
    list1 = sentence1.split()
    list2 = sentence2.split()

    #create new list to merge sentences
    new_list = [ ]
    l1 = 0
    l2 = 0

    #add to the new_list 2 words at a time until list length = 0, then add remaining from other list to new_list
    adding_to_list = True
    while adding_to_list:
        if l1 <= len(list1):
            new_list.extend(list1[:2])
            list1 = list1[2:]
            if len(list1) == l1:
                adding_to_list = False

        if l2 <= len(list2):
            new_list.extend(list2[:2])
            list2 = list2[2:]
            if len(list2) == l2:
                adding_to_list = False

    for x in list1:
        if len(list1) > 0:
            new_list.append(x)

    for x in list2:
        if len(list2) > 0:
            new_list.append(x)

    #take elements in new_list and join them together by spaces to form sentence
    new_sentence = " ".join(new_list)
    print(new_sentence)

merge2("The quick brown fox jumped over the lazy dog", "The cat ate the fish")
