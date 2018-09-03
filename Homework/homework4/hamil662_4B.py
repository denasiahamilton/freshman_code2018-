#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 4B

def search_sentence():
    to_continue = True
    while to_continue:
        #make sentence lower and split
        a_string = str(input("Enter a sentence: "))
        a_string = a_string.lower()
        a_string = a_string.split()

        #delete duplicate words in sentence
        for (i,x) in enumerate(a_string):
            string = x + " " + str(i)
            print(string)
            
        #ask to continue to enter
        ask_to_continue = str(input("Do you want to enter another sentence(Y/N)? "))
        ask_to_continue = ask_to_continue.lower()
        if ask_to_continue == "n":
           to_continue = False

search_sentence()
