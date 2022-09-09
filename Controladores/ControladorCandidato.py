from Modelos.Candidato2 import CandidatoBD
from db import db
from json import dumps

class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")


    def create(self, data):
        id = data['id']
        cedula = data['cedula']
        nombre = data['nombre']
        apellido = data['apellido']
        numlista = data['numlista']
        idpartido = data['idpartido']

        candidato = CandidatoBD(id=id, cedula=cedula, nombre=nombre, apellido=apellido, numlista=numlista,
                                idpartido=idpartido)
        db.session.add(candidato)
        db.session.commit()
        return {
            "id": id,
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "numlista": numlista,
            "idpartido": idpartido
        }

    def show(self, id):
        try:
            candidat = CandidatoBD.query.get(id)
            print(candidat)
            return
        except Exception as ex:
            return{'message': 'El candidato con ID: '+ id+' no existe'}


    def update(self, id, elCandidato):
            try:
                print("Actualizando Candidato con id ", id)
                candidatoupdate = CandidatoBD.query.get(id)
                candidatoupdate.cedula = elCandidato.get('cedula')
                candidatoupdate.nombre = elCandidato.get('nombre')
                candidatoupdate.apellido = elCandidato.get('apellido')
                candidatoupdate.numlista = elCandidato.get('numlista')
                candidatoupdate.idpartido = elCandidato.get('idpartido')
                db.session.add(candidatoupdate)
                db.session.commit()
                return {'message': 'Candidato con id: '+ id +' ha sido Actualizado'}

            except Exception as ex:
                return {'message': 'Candidato con id: '+ id +' no existe'}

    def delete(self, id):
        try:
            print()
            borrar = CandidatoBD.query.get(id)
            db.session.delete(borrar)
            db.session.commit()
            return {'message':'El candidato con el ID: '+ id+ ' ha sido eliminado'}
        except Exception as ex:
            return {'message': 'El candidato con ID: '+ id+' ha sido eliminado'}