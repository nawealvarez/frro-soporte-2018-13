def  max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


a = input("Primero\n")
b = input("Segundo\n")
c = input("Tercero\n")

a = int(a)
b = int(b)
c = int(c)

print("La suma es:"+" " + str(a+b+c))
print("El mayor es:"+" " + str( max_de_tres(a, b, c)))
