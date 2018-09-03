def reverse(new_list):
    a_list = [ ]
    for (i,v) in enumerate(new_list):
        i += 1
        a_list.append(new_list[-1])
        print (a_list)

    if a_list == new_list:
        return True
    else:
        return False

def ispalindrome():
    to_continue = True
    while to_continue:
        new_list = [ ]
        astring = str(input("Enter a string: "))
        astring = astring.lower()
        astring = astring.split()
        new_list.append(astring)

    reverse(new_list)
    while True:
        print(astring, "is a palindrome")
    else:
        print(astring, "is not a palindrome")

    ask_to_continue = str(input("Continue? (y/n) "))
    ask_to_continue = ask_to_continue.lower()
    if ask_to_continue == "n":
        to_continue = False
    else:
        to_continue = True 
ispalindrome()
