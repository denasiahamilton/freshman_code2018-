
def count_freq(a_string):
    the_occurance = { }
    for x in a_string:
        the_occurance[x] = the_occurance.get(x, 0) + 1
    print(the_occurance)

count_freq("1133Class")


"""
def add_fruit(inventory,fruit,quantity = 0):
    new_inventory = { }
    if fruit not in new_inventory:
        new_inventory[fruit] = quantity
    elif fruit in new_inventory:
        new_inventory[fruit] = quantity

    print(new_inventory)

add_fruit("new_inventory", "strawberries", 25)
"""
