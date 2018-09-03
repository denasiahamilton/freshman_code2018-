#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 3B

def main():
    print("Welcome to the Python Buffet, the hippest restaurant in town!")
    total_order = [ ] #will be list of all items ordered
    order = input("What would you like to order? ")
    order = order.lower()
    total_order.append(order)

    #anything_else loop -- keep asking "anything else" until user hits enter, then break
    #if user inputs same item twice, remove the duplicate
    while True:
        anything_else = input("Would you like to order anything else? ")
        anything_else = anything_else.lower()
        if anything_else in total_order:
            total_order.remove(anything_else)
            print("Oops. You must have ordered", anything_else, "again by accident!")
        elif anything_else == "":
            break
        total_order.append(anything_else)

    #print all ordered items in total_order list
    print("You have ordered the following: ")
    for (food) in total_order:
        print(food)

    #if 'burger' or 'soda' in food item in total_order list,
    #that item = 3 or 2, everything else is 5
    total_cost = 0
    for (food) in total_order:
        if 'burger' in food:
            total_cost += 3
        elif 'soda' in food:
            total_cost += 2
        else:
            total_cost += 5

    price = format(total_cost, ".2f")
    print("This will cost you a total of $", price)
    print("Thank you for your patronage!")

if __name__ == '__main__':
    main()
