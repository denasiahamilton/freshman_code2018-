#CSCI 1133 Homework 3
#Denasia Hamilton
#Problem 3C

def summation(lower_bound, upper_bound, function_name):
    first_list = [ ]
    first_list.append(lower_bound)

    #adds the values bewteen the lower bound and upper bound (and upper_bound) to the first_list
    count = 0
    total = 0
    while lower_bound < upper_bound:
        count += 1
        lower_bound += 1
        first_list.append(lower_bound)

    #perform summation according to function_name chosen by user
    if "square" == function_name:
        for (x) in first_list:
            square = x ** 2
            total += square
        print("The result of the summation is", total)

    elif "cube" == function_name:
        for (x) in first_list:
            cube = x ** 3
            total += cube
        print("The result of the summation is", total)

    elif "inverse" == function_name:
        for (x) in first_list:
            if (x) == 0:
                break
            else:
                inverse = 1 / x
                total += inverse
        if (x) == 0:
            print("UNDEFINED")
        else:
            print("The result of the summation is", total)

def main():
    lower_bound = int(input("Enter a lower bound for summation: "))
    upper_bound = int(input("Enter an upper bound for summation: "))
    function_name = str(input("Enter a function to be summed (square, cube, or inverse): "))
    #non-case sensitive
    function_name = function_name.lower()
    summation(lower_bound, upper_bound, function_name)

if __name__ == '__main__':
    main()
