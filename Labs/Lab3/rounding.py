def roundit(x):
    if x > 0: #add 0.5 if positive
        x = x + 0.5
    else:
        x = x - 0.5#subtract 0.5 if negative
    return int(x)
print(roundit(7.5))
