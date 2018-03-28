def superposicion(s, n):
    a = ""
    b = ""
    c = 0
    for i in range(0, len(s)):
        for j in range(0, len(n)):
            if s[i] == n[j]:
                c = c + 1
    if c >= 1:
        return True
    else:
        return False


# s = input("Ingrese letras separados por espacios:\n ")
# s = s.split()
# n = input("Ingrese letras separados por espacios:\n ")
# n = n.split()

assert superposicion("a b c", "j g a") == True
