import pymysql
from Connection import Connect

c = Connect()
conn = c.openConnection()

cur = conn.cursor()
caux = "SELECT * FROM persona"
cur.execute(caux)
a = cur.fetchall()


for i in cur.description:
    print(i[0], end=" | ")
print("")

for i in a:
    print(i)


cur.close()
c.closeConnection()
