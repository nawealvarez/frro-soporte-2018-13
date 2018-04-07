def Max(list):
    m = 0
    for n in list:
        if n > m:
            m = n
    return (m)

def Min(list):
    m = 99999999999999999
    for n in list:
        if n < m:
            m = n
    return (m)

def Main():
    n = input("Ingrese un nro: \n")
    list = []
    while n != "fin":
        n = int(n)
        list.append(n)
        n = input("Ingrese un nro: \n")

    min = Min(list)
    max = Max(list)

    print("Maximo: " + str(max))
    print("Minimo: " + str(min))

# Main()

assert max([132,3,43,0]) == 132
assert min([132,3,43,0]) == 0

