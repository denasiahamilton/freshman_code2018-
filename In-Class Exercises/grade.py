def grade():
    the_grade = float(input("Enter a percentage: "))
    if the_grade > float(str("93")):
        print("A")
    elif the_grade > float(str("90")):
        print("A-")
    elif the_grade > float(str("87")):
        print("B+")
    elif the_grade > float(str("83")):
        print("B")
    elif the_grade > float(str("80")):
        print("B-")
    elif the_grade > float(str("77")):
        print("C+")
    elif the_grade > float(str("73")):
        print("C")
    elif the_grade > float(str("70")):
        print("C-")
    elif the_grade > float(str("67")):
        print("D+")
    elif the_grade > float(str("60")):
        print("D")
    else:
        print("D-")
grade()
