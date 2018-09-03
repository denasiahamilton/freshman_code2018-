#CSCI 1133 Homework 7
#Denasia Hamilton
#Problem 7C

def mine_file(fname):
    text_file = open(fname, "r")
    count = 0
    d = { }
    unique_count = 0
    apostrophe_count = 0
    frequent = { }

    #reading one line at a time
    while True:
        thisLine = text_file.readline()
        if len(thisLine) == 0:
            break
        words = thisLine.lower()
        for ch in ",.!:;~?)(\/|-":
            words = words.replace(ch, " ")
        words = words.split()

        for x in words:
            count += 1
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

            if d[x] == 1:
                unique_count += 1

            apostrophe = "'"
            if apostrophe in x:
                apostrophe_count += 1

            if d[x] >= 5:
                frequent[x] = d[x]

    print("Word Count: ", count)
    print("Unique Word Count: ", unique_count)
    print("Apostrophe Count: ", apostrophe_count)


    values = list(frequent.values())
    values.sort()
    values.reverse()
    keys = list(frequent.keys())

    i = 0
    while i < len(values):
        for x in keys:
            if frequent[x] == values[i]:
                print(str(x) + ": " + str(frequent[x]))
                keys.remove(x)
        i +=1

    text_file.close()
mine_file("macbeth.txt")
