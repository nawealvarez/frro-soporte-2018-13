def contar_dig(n):
 if n > 9:
    n = n/10
    return 1 + contar_dig(n)
 elif n<=9:
    return 1


# print(str(contar_dig(1111)))

assert contar_dig(11) == 2
