import pymysql


conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='MySQL',
                       db='soporte_tp3')
cur = conn.cursor()

caux = "SELECT * FROM persona WHERE dni = '1111'"

cur.execute(caux)
a = cur.fetchall()


for i in cur.description:
    print(i[0], end=" | ")
print("")

for i in a:
    print(i)


cur.close()
conn.close()
