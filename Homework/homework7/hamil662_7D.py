#CSCI 1133 Homework 7
#Denasia Hamilton
#Problem 7D

def crime_report(fnameCVS):
    report_file = open(fnameCVS, "r")
    offenses = open("stealingOffenses.txt", "w")

    burglary = { }
    theft = { }
    robbery = { }

    while True:
        thisLine = report_file.readline()
        if len(thisLine) == 0:
            break
        parsing = thisLine.lower()
        parsing = parsing.split(",")


        if "burglary" in parsing[5]:
            for x in parsing[2]:
                if x not in burglary:
                    burglary[x] = 1
                else:
                    burglary[x] += 1

        if "theft" in parsing[5]:
            for x in parsing[2]:
                if x not in theft:
                    theft[x] = 1
                else:
                    theft[x] += 1

        if "robbery" in parsing[5]:
            for x in parsing[2]:
                if x not in robbery:
                    robbery[x] = 1
                else:
                    robbery[x] += 1

        burglary_sort = list(burglary.items())
        burglary_sort.sort()

        theft_sort = list(theft.items())
        theft_sort.sort()

        robbery_sort = list(robbery.items())
        robbery_sort.sort()

    district = 0
    amount = 0
    offenses.write("Burglaries by District: \n")
    for x in burglary_sort:
        (district, amount) = x
        offenses.write(district + ": " + str(amount) + " \n")
    offenses.write(" \n")

    offenses.write("Thefts by District: \n")
    for x in theft_sort:
        (district, amount) = x
        offenses.write(district + ": " + str(amount) + " \n")
    offenses.write(" \n")

    offenses.write("Robberies by District: \n")
    for x in robbery_sort:
        (district, amount) = x
        offenses.write(district + ": " + str(amount) + " \n")
    offenses.write(" \n")

    report_file.close()
    offenses.close()

crime_report("SacramentocrimeJanuary2006.csv")
