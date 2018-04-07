def es_primo(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
            elif n == x-1:
                return True

# print(str(es_primo(5)))
assert es_primo(6) == False
