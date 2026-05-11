from flask import Blueprint, request, jsonify
from models.egreso import Egreso
from models.ingreso import Ingreso
from config.db import db
from datetime import datetime

egreso_bp = Blueprint("egreso_bp", __name__)

@egreso_bp.route("/egresos", methods=["GET"])
def listar():
    datos = Egreso.query.all()
    resultado = []
    for e in datos:
        resultado.append({
            "id": e.id,
            "vehiculo_id": e.vehiculo_id,
            "hora_salida": e.hora_salida,
            "horas": e.horas,
            "total": e.total
        
        })
    return jsonify({
        "mensaje": "Lista de egresos",
        "egresos": resultado})

# POST:
@egreso_bp.route("/egreso/<int:vehiculo_id>", methods=["POST"])
def registrar_egreso(vehiculo_id):

    ingreso = Ingreso.query.filter_by(vehiculo_id=vehiculo_id).first()

    if not ingreso:
        return jsonify({"error": "No existe ingreso"}), 404

    hora_entrada = ingreso.hora_ingreso
    hora_salida = datetime.now()

    horas = (hora_salida - hora_entrada).total_seconds() / 3600
    horas = 1 if horas < 1 else round(horas)

    total = horas * 2000

    egreso = Egreso(
        vehiculo_id=vehiculo_id,
        hora_salida=hora_salida,
        horas=horas,
        total=total
    )

    db.session.add(egreso)
    db.session.delete(ingreso)
    db.session.commit()

    return jsonify({
        "message": "Egreso registrado",
        "total": total,
        "horas": horas
    })