#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 4D

import hamil662_4A

def main():
    #continuous program until user wants to quit
    to_continue = True
    while to_continue:

        #input an integer target, else reprompt
        isValid = True
        while isValid:
            target = input("Input target: ")
            #split so that if user hits space, it still accepts the target
            the_target = target.split()
            for x in the_target:
                if x.isnumeric():
                    isValid = False
                else:
                    print("Target must be an integer. Enter a valid target!")

        #input a "string" of numbers, then split for a list, then test to see if it is an integer
        anotherValid = True
        while anotherValid:
            the_list = input("Input list of numbers separated by a space: ")
            a_list = the_list.split()
            for x in a_list:
                if x.isnumeric():
                    anotherValid = False
                #if x in list is not an integer, reprompt until it is
                else:
                    print("The list can only contain integers. Enter a valid list!")
                    anotherValid = True

        #use function in imported file to print the number that sum to target
        the_sums = hamil662_4A.two_sums(a_list, the_target)
        print("The two numbers that sum up to", target, "are", the_sums)

        ask_to_continue = str(input("Would you like to enter another list and target (Y/N)? "))
        ask_to_continue = ask_to_continue.lower()
        if ask_to_continue == "n":
           to_continue = False

if __name__ == "__main__":
    main()
