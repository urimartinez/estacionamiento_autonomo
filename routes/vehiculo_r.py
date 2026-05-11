from flask import Blueprint, jsonify
from config.db import db
from models.vehiculo import Vehiculo

vehiculo_bp = Blueprint("vehiculo_bp", __name__)

# GET: listar vehículos
@vehiculo_bp.route("/vehiculos", methods=["GET"])
def get_vehiculos():
    vehiculos = Vehiculo.query.all()

    resultado = []

    for v in vehiculos:
        resultado.append({
            "id": v.id,
            "patente": v.patente,
            "marca": v.marca,
            "modelo": v.modelo})

    return jsonify({
        "mensaje": "Lista de vehículos",
        "vehiculos":resultado})