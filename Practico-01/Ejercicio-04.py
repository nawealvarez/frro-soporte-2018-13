def esVocOCon(l):
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or \
            l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
        return True
    else:
        return False


l = input("Ingrese una letra:\n")
print("Si devuelve True es vocal, sino devuelve False: " + " "+ str(esVocOCon(l)))


