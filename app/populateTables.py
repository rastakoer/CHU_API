from db import get_db_config, db_connect
import json

path = "/home/kevin/workspace/py-sql/brief_chu_api_flask/config.json"
config = get_db_config(path)

bdd = db_connect(config)
cursor = bdd.cursor()
dbOK = bdd.is_connected()



donnees = open("/home/kevin/workspace/py-sql/brief_chu_api_flask/app/data.json", "r")
donnees = json.load(donnees)
for table in donnees:
    for dictionnaire in donnees[table]:
        for valeur in list(dictionnaire.values()):
                     
            if table == "materiel":
                query = f"""INSERT INTO materiel(nom_du_produit, dimensions, etat) """
                query += f"""VALUES ("{valeur[0]}","{valeur[1]}","{valeur[2]}") ; """
                cursor.execute(query)
                bdd.commit()
            else : 
                query = f"""INSERT INTO employe_informatique(nom, prenom, age, profession) """
                query += f""" Values ('{valeur[0]}','{valeur[1]}','{valeur[2]}','{valeur[3]}');"""
                cursor.execute(query)
                bdd.commit()

cursor.close()
bdd.close()