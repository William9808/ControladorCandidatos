from flask import jsonify, Blueprint, request
import json
from Controladores.ControladorCandidato import ControladorCandidato

cont = ControladorCandidato()

candidato = Blueprint('candidato', __name__)


@candidato.route("/crearCandidato", methods=['POST'])
def create():
    data = request.get_json()
    info = cont.create(data)
    return jsonify(info)


@candidato.route("/mostrarCandidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json = cont.show(id)

    return jsonify(json)


@candidato.route("/modificarCandidato/<string:id>",methods=['PUT'])
def updateCandidato(id):
    data = request.get_json()
    json=cont.updateCandidato(id, data)
    return jsonify(json)


@candidato.route("/eliminarCandidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=cont.delete(id)
    return jsonify(json)



