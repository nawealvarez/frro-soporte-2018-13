<<<<<<< HEAD
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
=======
def es_palindromo(original):
    cadena = original[::-1]
    if cadena == original:
        return True
    else:
        return False


# print(str(es_palindromo('radar')))
assert es_palindromo('radar') == True
>>>>>>> 751396437412661de25b6bf82c4afdc1a98ae2f2
