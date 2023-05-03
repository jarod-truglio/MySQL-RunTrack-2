import mysql.connector

class Employe:
    
    def __init__(self, id=None, nom=None, prenom=None, salaire=None, id_service=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service
        
    @staticmethod
    def connect():
        cnx = mysql.connector.connect(user='root', password='6666',
                                      host='localhost',
                                      database='travail')
        return cnx
        
    def save(self):
        cnx = self.connect()
        cursor = cnx.cursor()
        if self.id is None:
            query = ("INSERT INTO employes "
                     "(nom, prenom, salaire, id_service) "
                     "VALUES (%s, %s, %s, %s)")
            values = (self.nom, self.prenom, self.salaire, self.id_service)
        else:
            query = ("UPDATE employes SET "
                     "nom = %s, "
                     "prenom = %s, "
                     "salaire = %s, "
                     "id_service = %s "
                     "WHERE id = %s")
            values = (self.nom, self.prenom, self.salaire, self.id_service, self.id)
        cursor.execute(query, values)
        cnx.commit()
        self.id = cursor.lastrowid
        cursor.close()
    
    @staticmethod
    def display_employes():
        cnx = Employe.connect()
        cursor = cnx.cursor()
        query = "SELECT * FROM employes"
        cursor.execute(query)
        for (id, nom, prenom, salaire, id_service) in cursor:
            print("id : {}, nom : {}, prenom : {}, salaire : {}, id_service : {}".format(id, nom, prenom, salaire, id_service))
        cursor.close()
        cnx.close()

Employe.display_employes()