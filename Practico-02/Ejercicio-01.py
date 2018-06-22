class Rectangulo:
    base = 3
    altura = 4

    def area(self):
        area = 0
        area = self.base * self.altura
        return area


x = Rectangulo()
# x.base = input("Ingrese la base del rectangulo:\n")
# x.altura = input("Ingrese la altura del rectangulo:\n")

# x.base = int(x.base)
# x.altura = int(x.altura))
# print(str(x.area()))
assert x.area() == 12

