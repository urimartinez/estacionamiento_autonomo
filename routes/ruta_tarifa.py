from flask import Blueprint, request, jsonify
from models.tarifa import Tarifa
from config.db import db

tarifa_bp = Blueprint("tarifa_bp", __name__)

# LISTAR TARIFAS
@tarifa_bp.route("/tarifas", methods=["GET"])
def listar_tarifas():

    tarifas = Tarifa.query.all()

    return jsonify(
        [t.serialize() for t in tarifas]
    )


# CREAR TARIFA
@tarifa_bp.route("/tarifa", methods=["POST"])
def crear_tarifa():

    data = request.json

    nueva_tarifa = Tarifa(
        descripcion=data["descripcion"],
        precio_hora=data["precio_hora"]
    )

    db.session.add(nueva_tarifa)

    db.session.commit()

    return jsonify({
        "message": "Tarifa creada"
    }), 201