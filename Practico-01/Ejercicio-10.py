def mas_larga(n):
 palabra_mayor = 0
 palabra_mostrar = ""
 for palabra in n:
     if palabra_mayor <= len(palabra):
         palabra_mostrar = palabra
         palabra_mayor = len(palabra)
 print(palabra_mostrar)


# n = input("Ingrese palabras separados por espacios:\n ")
# n = n.split()
# mas_larga(n)
assert mas_larga("a hola vpn") == "hola"
