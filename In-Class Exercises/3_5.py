
#RECURSION EXAMPLE 1, OUTPUT 4
def mystery(n1,n2):
    if n2 <= 0:
        return 1
    else:
        return(mystery(n1, n2-1) + mystery(n2, n2-1))

print(mystery(5,2))
