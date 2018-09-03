def rec(n):
    if n <= 1:
        return 2
    t = rec(n-1) * rec(n-2)
    return t

print(rec(4))
