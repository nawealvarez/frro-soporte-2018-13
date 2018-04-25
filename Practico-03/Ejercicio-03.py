import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='MySQL',
                       db='soporte_tp3')
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
conn.close()

