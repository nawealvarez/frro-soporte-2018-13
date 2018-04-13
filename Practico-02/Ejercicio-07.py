from datetime import date
import calendar


def inicio(f):
    if f >= date(f.year, 7, 1):
        fi = date(f.year, 7, 1)
    else:
        fi = date(f.year - 1, 7, 1)

    return fi


def fin(f):
    if f <= date(f.year, 6, 30):
        ff = date(f.year, 6, 30)
    else:
        ff = date(f.year + 1, 6, 30)

    return ff


def semana(f):
    if f >= date(f.year, 7, 1):
        fs = f.isocalendar()[1] - date(f.year, 7, 1).isocalendar()[1]
    else:
        fs = f.isocalendar()[1] - date(f.year - 1, 7, 1).isocalendar()[1]

    return fs



#fecha = date(2018, 7, 5)
#print(str(inicio(fecha)))
#fecha = date(2017, 8, 5)
#print(str(inicio(fecha)))


#VER SI ESTAN BIEN LAS SEMANAS - ISOCALENDAR EMPIEZA LOS JUEVES LAS SEMANAS
print(str(semana(date(2017, 1, 1))))


