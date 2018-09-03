#CSCI 1133 Homework 5
#Denasia Hamilton
#Problem 5B

def finding_base(decimal_number, the_base):
    #letters replace 10-15 in string
    conversion = '0123456789' + 'ABCDEF'

    #conversion[decimal_number] == place in the length of the string
    if decimal_number < the_base: #base case
        return conversion[decimal_number]

    #take the decimal_number, and divide it by the_base until the quotient = 0; this is final
    #once quotient = 0, take final & add remainder in type(str) based on conversion, return string
    #if remainder < 9, use letter from conversion
    else:
        final = finding_base(decimal_number//the_base, the_base) #division
        remainder = decimal_number % the_base #module, remainder
        return str(final) + conversion[remainder]

def main():
    decimal_number = int(input("Enter your decimal number: " ))
    the_base = int(input("Enter the base you want to convert to: "))
    print(decimal_number, "in base", the_base, "is", finding_base(decimal_number, the_base))

if __name__ == "__main__":
    main()
