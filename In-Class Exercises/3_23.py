def number_of_letters(string1, string2):
    string1 = set(string1)
    string2 = set(string2)

    count = 0
    for x in string1:
        if x not in string2:
            count +=1
    print(count)

number_of_letters("computer", "hello")
