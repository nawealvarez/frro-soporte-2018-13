def sumawhile(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    return sum


# print(str(sumawhile(5)))
assert sumawhile(5) == 15
