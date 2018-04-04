def es_palindromo(original):
    cadena = original[::-1]
    if cadena == original:
        return True
    else:
        return False


# print(str(es_palindromo('radar')))
assert es_palindromo('radar') == True
