import pymysql
from Connection import Connect
import jsonpickle  # Descargar libreria JSONPickle

c = Connect()
conn = c.openConnection()

caux = "SELECT * FROM PERSONA"
cur = conn.cursor()

cur.execute(caux)
data = jsonpickle.encode(cur.fetchall())

print(data)

cur.close()
c.closeConnection()
