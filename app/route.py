from flask import render_template, request , jsonify
from app import app
from .db import get_db_config, db_connect
import requests


path = "/home/kevin/workspace/py-sql/brief_chu_api_flask/config.json"
config = get_db_config(path)

bdd = db_connect(config)
cursor = bdd.cursor()
dbOK = bdd.is_connected()

#------------------------------------------------------------------
#   Page web
#------------------------------------------------------------------
@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        try:
            matos = requests.get("http://127.0.0.1:5000/materiel/")
            matos = matos.json()
            employes = requests.get("http://127.0.0.1:5000/employe_informatique/")
            employes = employes.json()
            return render_template('index.html', matos=matos, employes=employes)
        
        except Exception as e:
            return {"erreur" : e}


#------------------------------------------------------------------
#   Routes API materiel
#------------------------------------------------------------------

@app.route('/materiel/', methods=["GET"])
def get_db_matos():
    
    try:
        query=f"""SELECT * FROM materiel ;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel/', methods=["POST"])
def add_matos():
    record= request.get_json()

    try:
        query=f"""INSERT INTO materiel(nom_du_produit, dimensions, etat) """
        query += f""" VALUES ("{record['nom']}","{record['dim']}", "{record['etat']}");"""
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_matos()
        return result_db

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel/', methods=["PUT"])
def modif_matos():
    record= request.get_json()

    try:
        query=f"""UPDATE materiel SET nom_du_produit="{record['nom']}","""
        query += f""" dimensions="{record['dim']}", etat="{record['etat']}" """
        query += f"""  WHERE id={record['id']} ; """
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_matos()
        return result_db

    except Exception as e:
        return {"erreur" : e}

@app.route('/materiel/', methods=["DELETE"])
def sup_matos():
    record= request.get_json()

    try:
        query=f"""DELETE FROM materiel WHERE id='{record['id']}' ;"""
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_matos()
        return result_db

    except Exception as e:
        return {"erreur" : e}


#------------------------------------------------------------------
#   Routes API employés informatique
#------------------------------------------------------------------
@app.route('/employe_informatique/', methods=["GET"])
def get_db_employe():
    
    try:
        query=f"""SELECT * FROM employe_informatique ;"""
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)

    except Exception as e:
        return {"erreur" : e}

@app.route('/employe_informatique/', methods=["POST"])
def add_employe():
    record= request.get_json()

    try:
        query=f"""INSERT INTO employe_informatique(nom, prenom, age, profession) """
        query += f""" VALUES ("{record['nom']}","{record['prenom']}", """
        query += f""" {record['age']}, "{record['profession']}");"""
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}


@app.route('/employe_informatique/', methods=["PUT"])
def modif_employe():
    record= request.get_json()

    try:
        query=f"""UPDATE employe_informatique SET nom="{record['nom']}","""
        query += f""" prenom="{record['prenom']}", age={record['age']} """
        query += f"""  WHERE id={record['id']} ; """
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}


@app.route('/employe_informatique/', methods=["DELETE"])
def sup_employe():
    record= request.get_json()

    try:
        query=f"""DELETE FROM employe_informatique WHERE id={record['id']} ;"""
        cursor.execute(query)
        bdd.commit()
        result_db = get_db_employe()
        return result_db

    except Exception as e:
        return {"erreur" : e}