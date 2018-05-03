import pymysql
from Connection import Connect

c = Connect()
conn = c.openConnection()

cur = conn.cursor()
caux = "UPDATE persona SET nombre='sergio' WHERE idPersona=3;"

cur.execute(caux)

conn.commit()

cux = "SELECT * FROM persona WHERE idPersona = 3"

cur.execute(cux)
a = cur.fetchall()


for i in cur.description:
    print(i[0], end=" | ")
print("")

for i in a:
    print(i)

cur.close()
c.closeConnection()
