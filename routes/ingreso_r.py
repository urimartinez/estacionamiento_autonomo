from flask import Blueprint, request, jsonify
from models.ingreso import Ingreso
from config.db import db
from datetime import datetime
from models.vehiculo import Vehiculo

ingreso_bp = Blueprint("ingreso_bp", __name__)

@ingreso_bp.route("/ingreso", methods=["GET"])
def listar_ingresos():

    ingresos = Ingreso.query.all()

    resultado = []

    for i in ingresos:
        resultado.append({
            "id": i.id,
            "vehiculo_id": i.vehiculo_id,
            "hora_ingreso": i.hora_ingreso
        })

    return jsonify({
        "mensaje": "Lista de ingresos",
        "ingresos": resultado
    })
# POST:
@ingreso_bp.route("/ingreso", methods=["POST"])
def registrar_ingreso():

    data = request.json

    vehiculo_id = data.get("vehiculo_id")

    if not vehiculo_id:
        return jsonify({"error": "Falta vehiculo_id"}), 400

    # opcional: verificar que exista el vehículo
    vehiculo = vehiculo.query.get(vehiculo_id)

    if not vehiculo:
        return jsonify({"error": "Vehículo no existe"}), 404
    existe = Ingreso.query.filter_by(
        vehiculo_id=vehiculo_id
    ).first()
    if existe:
        return jsonify({"error": "El vehiculo ya ingreso"}),400
    nuevo = Ingreso(
        vehiculo_id=vehiculo_id,
        hora_ingreso=datetime.now()
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "mensaje": "Ingreso registrado",
        "vehiculo_id": vehiculo_id,
        "hora_ingreso": nuevo.hora_ingreso
    })
