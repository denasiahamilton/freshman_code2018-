#CSCI 1133 Homework1
#Denasia Hamilton
#Problem 1D

def absError(act_value, measured_value):
    absError = abs(act_value - measured_value)
    return round(absError, 6)

print(absError(3.2,3.3))

def relError(act_value, measured_value):
    relError = absError(act_value, measured_value) / act_value
    return round(relError, 6)

print(relError(3.2,3.3))
