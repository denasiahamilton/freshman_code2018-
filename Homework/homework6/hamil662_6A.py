#CSCI 1133 Homework 6
#Denasia Hamilton
#Problem 6A

FOOD = {"pizza": 127829, "chicken": 127831, "apple": 127822, "peach": 127825,
     "cherry": 127826, "roasted sweet potato": 127840, "pineapple": 127821,
     "cookie": 127850, "bread": 127838, "lemon": 127819, "banana":127820,
     "strawberry": 127827}

def addItem(d,item):
    #if item is in dictionary, add += 1, else establish d[item] = 1
    if item not in d:
        d[item] = 1
    else:
        d[item] = d[item] + 1

def subItem(d,item):
    #if item is in dictionary, subtract -= 1
    if item in d:
        d[item] = d[item] - 1
        if d[item] == 0:
            del d[item]

def show(d):
    #print d; item and display values with unicode decimal
    for item in d:
        if item in FOOD:
            print (item + " " + chr(FOOD[item]) * d[item])
        else:
            print(item + " " + str(d[item]))

def lookup(d,item):
    #if item is in dictionary, print item and unicode decimal (amount = value)
    if item in d:
        if item in FOOD:
            print (item + " " + chr(FOOD[item]) * d[item])
        else:
            print(item + " " + str(d[item]))

def main():
    d = {}
    while True:
        item = str(input("=> "))
        if "add" in item:
            item = item[4: ]
            addItem(d,item)
        elif "sub" in item:
            item = item[4: ]
            subItem(d,item)
        elif "show" in item:
            show(d)
        elif "lookup" in item:
            item = item[7: ]
            lookup(d,item)
        elif "quit" in item:
            break

if __name__ == "__main__":
    main()
