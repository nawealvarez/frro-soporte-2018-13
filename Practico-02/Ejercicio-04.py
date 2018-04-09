from datetime import date


class Persona:
    nombre = "Lautaro"
    fecha_nac = date(1995, 5, 15)
    sexo = 'H'
    peso = 75
    altura = 1.90
    dni = 39306134


class Estudiante(Persona):
    carrera = "Ingenieria en Sitemas de la Informacion"
    ingreso = date(2014, 3, 12)
    materias_carrera = 45
    materias_aprobadas = 20

    def avance(self):
        porcentaje = 0
        porcentaje = (float("%.2f" % ((self.materias_aprobadas * 100) / self.materias_carrera)))
        return porcentaje

    def edad_ingreso(self):
        edad_ingreso = 0
        edad_ingreso = self.ingreso.year - self.fecha_nac.year
        return edad_ingreso


x = Estudiante()
# print("La fecha de nacimiento es:" + " " + str(x.fecha_nac) + ", ingresó con" + " " + str(x.edad_ingreso()) + " años" +
#    " tiene aprobado el " + str(x.avance()) + " % de la carrera")
assert x.avance() == 44.44 and x.edad_ingreso() == 19
