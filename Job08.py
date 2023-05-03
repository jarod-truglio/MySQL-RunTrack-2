import mysql.connector

cnx = mysql.connector.connect(user='root', password='6666',
                              host='localhost', database='zoo')

cursor = cnx.cursor()

query = ("INSERT INTO cage "
         "(superficie, capacite_max) "
         "VALUES (%s, %s)")

values = [    (30, 5),    (40, 10),    (50, 15)]

cursor.executemany(query, values)
cnx.commit()

print(cursor.rowcount, "cages ajoutées.")

query = ("SELECT cage.id, cage.superficie, COUNT(animal.id) "
         "FROM cage "
         "LEFT JOIN animal "
         "ON cage.id = animal.id_cage "
         "GROUP BY cage.id "
         "HAVING COUNT(animal.id) > 0")

cursor.execute(query)
cages_avec_animaux = cursor.fetchall()

print("Cages avec des animaux :")
for cage in cages_avec_animaux:
    print("ID :", cage[0], "Superficie :", cage[1], "Nombre d'animaux :", cage[2])

query = ("SELECT cage.id, cage.superficie "
         "FROM cage "
         "LEFT JOIN animal "
         "ON cage.id = animal.id_cage "
         "WHERE animal.id_cage IS NULL")

cursor.execute(query)
cages_sans_animaux = cursor.fetchall()

print("\nCages sans animaux ss :")
for cage in cages_sans_animaux:
    print("ID :", cage[0], "Superficie :", cage[1])

animals = [
    {
        'nom': 'Zazou',
        'race': 'Perroquet',
        'id_cage': cages_sans_animaux[0][0],
        'date_naissance': '2021-01-01',
        'pays_origine': 'Brésil'
    },
    {
        'nom': 'Rex',
        'race': 'Chien',
        'id_cage': cages_sans_animaux[1][0],
        'date_naissance': '2019-05-10',
        'pays_origine': 'France'
    },
    {
        'nom': 'Garfield',
        'race': 'Chat',
        'id_cage': cages_sans_animaux[2][0],
        'date_naissance': '2020-07-20',
        'pays_origine': 'États-Unis'
    }
]

query = ("INSERT INTO animal "
         "(nom, race, id_cage, date_naissance, pays_origine) "
         "VALUES (%(nom)s, %(race)s, %(id_cage)s, %(date_naissance)s, %(pays_origine)s)")

for animal in animals:
    cursor.execute(query, animal)

cnx.commit()

print(cursor.rowcount, "animaux ajoutés.")

cursor.close()
cnx.close()