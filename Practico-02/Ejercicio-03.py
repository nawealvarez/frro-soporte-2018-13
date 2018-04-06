import random


class Persona:
    nombre = "Lautaro"
    edad = 16
    sexo = 'H'
    peso = 345
    altura = 1.90
    dni = "No definido"

    def es_mayor_edad(self):
        if self.edad > 18:
            return True
        else:
            return False

    def print_data(self):
        print("Nombre: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("Sexo: " + str(self.sexo))
        print("Peso: " + str(self.peso))
        print("Altura: " + str(self.altura))
        print("DNI: " + str(self.dni))

    def generar_dni(self):
        dni = random.randrange(100000000)
        self.dni = dni

    def __init__(self):
        self.generar_dni()


persona = Persona()
persona.print_data()
assert persona.es_mayor_edad() == False




