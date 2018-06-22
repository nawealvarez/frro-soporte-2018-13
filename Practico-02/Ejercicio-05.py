from datetime import date


class Persona:
    nombre = "Lautaro"
    fecha_nac = date(1995, 5, 15)
    sexo = 'H'
    peso = 75
    altura = 1.90
    dni = 39306134


class Estudiante(Persona):
    carrera = "Ingenieria en Sitemas de Informacion"
    ingreso = date(2014, 3, 12)
    materias_carrera = 45
    materias_aprobadas = 20

    def avance(self):
        porcentaje = (float("%.2f" % ((self.materias_aprobadas * 100) / self.materias_carrera)))
        return porcentaje

    def edad_ingreso(self):
        edad_ingreso = self.ingreso.year - self.fecha_nac.year
        return edad_ingreso


def cantidad_en_carreras(a=[]):
    carreras = []
    alumnos_en_carrera = {}

    for x in a:
        if x.carrera not in carreras:
            carreras.append(x.carrera)

    for y in carreras:
          cant = 0
          for x in a:
             if x.carrera == y:
                 cant = cant + 1
                 alumnos_en_carrera[x.carrera] = cant

    return alumnos_en_carrera


e1 = Estudiante()
e2 = Estudiante()
e3 = Estudiante()
e4 = Estudiante()
e5 = Estudiante()

e3.carrera = "Ingenieria Quimica"
e4.carrera = "Ingenieria Quimica"
e5.carrera = "Ingenieria Electrica"

estudiantes = [e1,e2,e3,e4,e5]

c = cantidad_en_carreras(estudiantes)

#for k,v in c.items():
#    print(k, ":", v)
#

assert list(c.keys()) == ["Ingenieria en Sitemas de Informacion", "Ingenieria Quimica", "Ingenieria Electrica"] and list(c.values()) == [2,2,1]
