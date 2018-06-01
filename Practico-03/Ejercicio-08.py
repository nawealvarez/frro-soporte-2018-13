import pymysql
from Connection import Connect


c = Connect()
conn = c.openConnection()

cur = conn.cursor()

caux = "INSERT INTO personapeso (idPersona, fecha, peso) "


cur.execute(caux)
conn.commit()
cur.close()
c.closeConnection()
