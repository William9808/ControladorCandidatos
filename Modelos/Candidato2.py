from db import db


class CandidatoBD(db.Model):

    __tablename__ = "Candidatos"

    id = db.Column(db.Integer, primary_key = True)
    cedula = db.Column(db.VARCHAR)
    nombre = db.Column(db.String())
    apellido = db.Column(db.String())
    numlista = db.Column(db.Integer)
    idpartido = db.Column(db.Integer)

    def __init__(self, id, cedula, nombre, apellido, numlista, idpartido):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.numlista = numlista
        self.idpartido = idpartido

    def __repr__(self):
        return f" id: {self.id}, cedula: {self.cedula}, " \
               f"nombre: {self.nombre}, apellido: {self.apellido}, numlista: {self.numlista}, idpartido: {self.idpartido}"
