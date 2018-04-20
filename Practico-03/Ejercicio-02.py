import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='MySQL',
                       db='soporte_tp3')

cur = conn.cursor()

dni = "1234"
fechaNacimiento = "19960102"
nombre = "Pepe"
altura = "150"

caux = "INSERT INTO persona (dni, fechaNacimiento, nombre, altura ) VALUES ({0},{1},{2},{3})".format(repr(dni), repr(fechaNacimiento), repr(nombre), repr(altura))

cur.execute(caux)

conn.commit()

cur.close()
conn.close()
