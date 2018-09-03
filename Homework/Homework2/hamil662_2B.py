#CSCI 1133 Homework2
#Denasia Hamilton
#Problem 2B

def zodiac():
    month = int(input("Month of birth: "))
    date = int(input("Day of birth: "))
    isValid = True
    while isValid:
        isValid = False
        if month == 1 and date in range(20,32) or month == 2 and date in range(1,19):
            print("Aquarius")
        elif month == 2 and date in range(20,29) or month == 3 and date in range(1,21):
            print ("Pisces")
        elif month == 3 and date in range(22,32) or month == 4 and date in range(1,20):
            print("Aries")
        elif month == 4 and date in range(21,31) or month == 5 and date in range(1,21):
            print("Taurus")
        elif month == 5 and date in range(22,32) or month == 6 and date in range(1,21):
            print("Gemini")
        elif month == 6 and date in range(22,31) or month == 7 and date in range(1,23):
            print("Cancer")
        elif month == 7 and date in range(24,32) or month == 8 and date in range(1,23):
            print("Leo")
        elif month == 8 and date in range(24,32) or month == 9 and date in range(1,23):
            print("Virgo")
        elif month == 9 and date in range(24,31) or month == 10 and date in range(1,23):
            print("Libra")
        elif month == 10 and date in range(24,32) or month == 11 and date in range(1,22):
            print("Scorpio")
        elif month == 11 and date in range(23,31) or month == 12 and date in range(1,22):
            print("Sagittarius")
        elif month == 12 and date in range(23,32) or month == 1 and date in range(1,19):
            print("Aquarius")
        else:
            print("Invalid Date")
            isValid = True
            month = int(input("Month of birth: "))
            date = int(input("Day of birth: "))
zodiac()
