from flask import Blueprint, request, jsonify
from models.ingreso import Ingreso
from config.db import db
from datetime import datetime

ingreso_bp = Blueprint("ingreso_bp", __name__)

@ingreso_bp.route("/ingreso", methods=["GET"])
def crear_ingreso():
    vehiculo_id = request.args.get("vehiculo_id")

    if not vehiculo_id:
        return jsonify({"error": "Falta vehiculo_id"}), 400

    nuevo = Ingreso(
        vehiculo_id=vehiculo_id,
        hora_ingreso=datetime.now()
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({
        "mensaje": "Ingreso registrado",
        "vehiculo_id": vehiculo_id
    })