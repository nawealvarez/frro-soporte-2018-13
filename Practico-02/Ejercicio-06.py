from datetime import date


class Persona:
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        if date.today().month > self.nacimiento.month:
            edad = date.today().year - self.nacimiento.year
        elif date.today().month == self.nacimiento.month and date.today().day >= self.nacimiento.day:
            edad = date.today().year - self.nacimiento.year
        else:
            edad = date.today().year - self.nacimiento.year - 1
        return edad


fecha = date(1995, 11, 18)
pers = Persona(fecha)

# print("La edad de la persona es: " + str(pers.edad()) + " años")

assert pers.edad() == 22

