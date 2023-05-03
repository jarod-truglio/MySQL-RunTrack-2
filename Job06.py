import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost',
                              database='LaPlateforme')

cursor = cnx.cursor()

query = "SELECT SUM(capacite) FROM salles"
cursor.execute(query)
result = cursor.fetchone()[0]

print("La somme des capacités des salles est de {} personnes.".format(result))

cursor.close()
cnx.close()