from flask import Blueprint, request, jsonify
from models.espacio import Espacio
from config.db import db

espacio_bp = Blueprint("espacio_bp", __name__)
# Listar precios

@espacio_bp.route("/espacios", methods=["GET"])
def listar_espacios():

    espacios = Espacio.query.all()

    return jsonify(
        [e.serialize() for e in espacios]
    )

# Se crea el espacio
@espacio_bp.route("/espacio", methods=["POST"])
def crear_espacio():

    data = request.json

    nuevo_espacio = Espacio(
        numero=data["numero"]
    )

    db.session.add(nuevo_espacio)

    db.session.commit()

    return jsonify({
        "message": "Espacio creado"
    }), 201