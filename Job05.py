import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost',
                              database='LaPlateforme')

cursor = cnx.cursor()

etage_query = "SELECT SUM(superficie) FROM etage"
cursor.execute(etage_query)
etage_superficie = cursor.fetchone()[0]

print("La superficie de La Plateforme est de {} m2".format(etage_superficie))

cursor.close()
cnx.close()
