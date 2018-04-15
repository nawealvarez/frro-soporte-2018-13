from datetime import datetime

class Persona():
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        edad = (datetime.now() - self.nacimiento).days
        years = (int(edad/365))
        return years

date = datetime(2009, 1, 6, 15, 8, 24, 78915)
pers = Persona(date)

# print("La edad de la persona es: " + str(pers.edad()) + " años")

assert pers.edad() == 9

