import cmath


class Circulo:
    radio = 4

    def area(self):
        area = 0
        area = cmath.pi * (self.radio**2)
        return float("%.2f" % area)

    def perimetro(self):
        perimetro = 0
        perimetro = 2 * cmath.pi * self.radio
        return perimetro


x = Circulo()
# print("El area es:" + " " + str(x.area()) + " " +"y el perimetro es:" + " " + str(x.perimetro()))

#assert x.area() == 50.26
#assert x.perimetro() == 25.132741228718345
print(x.area())
# print(x.perimetro())

