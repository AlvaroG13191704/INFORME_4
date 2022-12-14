
from flask_cors import CORS, cross_origin

from flask import Flask, request, redirect, jsonify


import json
from SQL_request import create_user,get_users,delete_user,edit_user

app=Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def prueba():
    return jsonify({"mensaje":"hola"})

@cross_origin
@app.route("/insert", methods=["POST"])
def insertar():
    info = json.loads(request.data)
    create_user(info["id"], info["nombre"], info["edad"], info["genero"], info["tel"])
    return info


@cross_origin
@app.route("/select", methods=["GET"])
def obtener():
    return jsonify(get_users())


@app.route("/delete", methods=["DELETE"])
def eliminar():
    info = json.loads(request.data)
    delete_user(info["id"])
    return info


@app.route("/update", methods=["PUT"])
def actualizar():
    info = json.loads(request.data)
    edit_user(info["id"], info["nombre"], info["edad"], info["genero"], info["tel"])
    return info




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    