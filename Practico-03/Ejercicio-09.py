import pymysql
from Connection import Connect

dni = input("Ingrese el DNI de la persona a buscar: ")

c = Connect()
conn = c.openConnection()
cur = conn.cursor()

caux = "select * from persona where dni = '{}'".format(dni)

try:
    cur.execute(caux)
    pers = cur.fetchone()
    cur.close()
    if pers[0] is None:
        print("No existe una persona con ese DNI")
    else:
        #for p in pers:
        print(pers)
        cur2 = conn.cursor()
        caux = "select * from personacorporal where idPersona = {}".format(pers[0])
        cur2.execute(caux)
        peso = cur2.fetchall()
        cur2.close()
        for p in peso:
            print(p)
except Exception as e:
    print('Got error {!r}, errno is {}'.format(e, e.args[0]))
finally:
    c.closeConnection()



