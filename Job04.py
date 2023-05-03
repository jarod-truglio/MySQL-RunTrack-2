import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost',
                              database='LaPlateforme')

cursor = cnx.cursor()

etage_query = "SELECT * FROM etage"
salles_query = "SELECT * FROM salles"
cursor.execute(salles_query)
print("Salles :")
for (id, nom, id_etage, capacite) in cursor:
    print("{} - étage {} - capacité {}".format(nom, id_etage, capacite))

print("----------")

cursor.execute(etage_query)
print("\nÉtages :")
for (id, nom, numero, superficie) in cursor:
    print("{} - numéro {} - superficie {}".format(nom, numero, superficie))

cursor.close()
cnx.close()