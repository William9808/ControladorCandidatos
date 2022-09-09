from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from db import db
from Routes.CandidatoRoute import candidato
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:cRX8POI1@localhost:5432/Candidatos"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(candidato)


def loadFileConfig():
    with open('../ControladorCandidatos/config.json') as f:
        data = json.load(f)
        return data


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running on: " + "http://"+dataConfig["url_backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url_backend"], port=dataConfig["port"])


