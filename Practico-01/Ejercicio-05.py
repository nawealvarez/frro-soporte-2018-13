def multip(n):
    total = 1
    for i in n:
        total = total * int(i)
    print(str(total))


# n = input("Ingrese numeros separados por espacios:\n ")
# n = n.split()
#
# print("El resultado es:" + " " + str(multip(n)))

assert multip("3 2 4") == 24
