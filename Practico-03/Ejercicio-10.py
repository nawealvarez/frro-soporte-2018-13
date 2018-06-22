import pymysql
from Connection import Connect
import jsonpickle  # Descargar libreria JSONPickle


c = Connect()
conn = c.openConnection()
cur = conn.cursor()

caux = "SELECT * FROM PERSONA AS P LEFT JOIN PERSONACORPORAL AS PC ON P.idPersona = PC.idPersona"
cur = conn.cursor()

cur.execute(caux)
data = jsonpickle.encode(cur.fetchall())

print(data)

cur.close()
c.closeConnection()
