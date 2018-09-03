
def mul(a,b):
    count = 0
    product = 0
    while count < b:
        count += 1
        product = a + product
    return product
print(mul(3,5))
