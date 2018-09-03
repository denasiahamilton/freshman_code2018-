#CSCI 1133 Homework1
#Denasia Hamilton
#Problem 1B

print ("Welcome to the Currency Conversion Program!!")
us_dollars = float(input("Enter an amount in U.S Dollars: $ ",))
dollars = format(us_dollars, ".2f")
euro = format(us_dollars * 0.83, ".2f")  #euro
print ("$", dollars, "=", euro, "euro")
yen = format(us_dollars * 111.14, ".2f") #yen
print ("$", dollars, "=", yen, "yen")
bitcoin = format(us_dollars / 13161.62, ".2f")
print ("$", dollars, "=", bitcoin, "bitcoin") #bitcoin
