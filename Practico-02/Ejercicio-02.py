import cmath


class Circulo:
    radio = 4

    def area(self):
        area = 0
        area = (float("%.2f" % cmath.pi)) * (self.radio**2)
        return area

    def perimetro(self):
        perimetro = 0
        perimetro = 2 * (float("%.2f" % cmath.pi)) * self.radio
        return perimetro


x = Circulo()
# print("El area es:" + " " + str(x.area()) + " " +"y el perimetro es:" + " " + str(x.perimetro()))

assert x.area() == 50.24 and x.perimetro() == 25.12


