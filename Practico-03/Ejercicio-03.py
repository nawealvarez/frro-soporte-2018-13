import pymysql
from Connection import Connect

c = Connect()
conn = c.openConnection()

cur = conn.cursor()

caux = "DELETE FROM persona WHERE idPersona = '4'"
cux = "SELECT * FROM persona"

cur.execute(caux)
cur.execute(cux)
a = cur.fetchall()

for i in cur.description:
    print(i[0], end=" | ")
print("")

for i in a:
    print(i)

conn.commit()

cur.close()
c.closeConnection()

