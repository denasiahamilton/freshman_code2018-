def double_stuff(a_list):
    new_list = []
    for i in range(len(a_list)):
        new_list.append(2 * a_list[i])
    return new_list

things = [2,5,9]
result = double_stuff(things)
print (result)
print (things)
