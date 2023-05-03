import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost',
                              database='LaPlateforme')

cursor = cnx.cursor()

query = "SELECT * FROM etudiants"
cursor.execute(query)

for (id, nom, prenom, age, email) in cursor:
    print("{} {} ({}) - {}".format(prenom, nom, age, email))

cursor.close()
cnx.close()