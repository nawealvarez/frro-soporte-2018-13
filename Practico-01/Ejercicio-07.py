def inversa(s):
    a = ""
    for x in range(1, (len(s) + 1)):
        a = a + s[-x]
    return(a)

def chequearInversa(i):
    inv = inversa(i)
    if inv == i:
        print("Es un palindromo")
    else:
        print("No es un palindromo")


s = input("Ingrese una frase: \n")
chequearInversa(s.lower())

assert chequearInversa("neuquen")
