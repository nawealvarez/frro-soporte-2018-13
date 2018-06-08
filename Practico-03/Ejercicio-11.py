import math

x = input("Ingrese dividendo: ")
y = input("Ingrese dividendo: ")

try:
    x = int(x)
    y = int(y)
    d = x/y
    print(str(d))
except ValueError as type:
    print(str(type))
    print("Divide({},{})").format(str(x), str(y))
except ArithmeticError as arit:
    print(str(arit))
    print("Divide({},{})").format(str(x), str(y))
except ZeroDivisionError as zero:
    print(str(zero))
    print("Divide({},{})").format(str(x), str(y))
