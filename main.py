import json
import pymysql
from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)


@app.route("/insertar", methods=["POST"])
def insertar():
    info = json.loads(request.data)
    insert(info["id"], info["nombre"])
    return info


@app.route("/select/", methods=["GET"])
def obtener():
    return json.dumps(select())


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)



