import pymysql
from Connection import Connect
from datetime import datetime
persona = 1
peso = 20

c = Connect()
conn = c.openConnection()

cur = conn.cursor()

caux = "select count(idPersona) from persona where idPersona= '{}'".format(persona)
cur.execute(caux)

a = cur.fetchone()
cur.close()
if a != 0:
    caux = "select fecha from personacorporal where idPersona = '{}'".format(persona)
    cur2 = conn.cursor()
    cur2.execute(caux)
    fechas = cur2.fetchall()
    cur2.close()
    esValido = True
    for f in fechas:
        if f > datetime.now():
            valido = False
    if esValido:
        caux = "insert into personacorporal(idPersona, fecha, peso) values({0}, '{1}', {2})".format(persona, datetime.today().strftime('%Y-%m-%d'),peso)
        cur3 = conn.cursor()
        cur3.execute(caux)
        print("Se ha guardado con exito!")
        cur3.close()
c.closeConnection()
