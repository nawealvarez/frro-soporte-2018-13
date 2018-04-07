def mas_larga(n):
 palabra_mayor = 0
 palabra_mostrar = ""
 n = n.split()
 for palabra in n:
     #print ()
     if palabra_mayor <= len(palabra):
         palabra_mostrar = palabra
         palabra_mayor = len(palabra)
 return (palabra_mostrar)


# n = input("Ingrese palabras separados por espacios:\n ")
# n = n.split()
# mas_larga(n)
assert mas_larga("hola señor kiosquero") == "kiosquero"
