def inversa(s):
    a = ""
    for x in range(1, (len(s) + 1)):
        a = a + s[-x]
    return(a)


s = input("Ingrese una oracion: \n")

s = inversa(s)

print("La oracion al reves es:" + " " + s)
