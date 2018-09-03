def emul(a,b):
    count = 0
    product = 0
    while count < b:
        count =+ 1
        if b % 2 == 1:
            product = product + a
    return product
print(emul(22,17))
