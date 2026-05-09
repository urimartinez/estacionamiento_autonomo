from flask import Blueprint, request, jsonify
from models.egreso import Egreso
from config.db import db
from datetime import datetime

egreso_bp = Blueprint("Egresos_bp", __name__)

# LISTAR
@egreso_bp.route("/egresos", methods=["GET"])
def listar():
    datos = Egreso.query.all()
    return jsonify([i.serialize() for i in datos])

# CREAR (IMPORTANTE)
@egreso_bp.route("/egreso", methods=["POST"])
def crear():
    data = request.json

    nuevo = Egreso(
        vehiculo_id=data["vehiculo_id"]
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({"message": "Ingreso creado"}), 201


#

from flask import Blueprint, jsonify
from models.egreso import Egreso
from models.ingreso import Ingreso
from config.db import db
from datetime import datetime

egreso_bp = Blueprint("egreso_bp", __name__)

@egreso_bp.route("/egreso/<int:vehiculo_id>", methods=["POST"])
def registrar_egreso(vehiculo_id):

    ingreso = Ingreso.query.filter_by(vehiculo_id=vehiculo_id).first()

    if not ingreso:
        return jsonify({"error": "No existe ingreso"}), 404

    hora_entrada = ingreso.hora_ingreso
    hora_salida = datetime.now()

    horas = (hora_salida - hora_entrada).total_seconds() / 3600

    if horas < 1:
        horas = 1
    else:
        horas = round(horas)

    tarifa_por_hora = 2000  # simple (como el profe)
    total = horas * tarifa_por_hora

    egreso = Egreso(
        vehiculo_id=vehiculo_id,
        hora_salida=hora_salida,
        horas=horas,
        total=total
    )

    db.session.add(egreso)

    # eliminar ingreso (como liberar lugar)
    db.session.delete(ingreso)

    db.session.commit()

    return jsonify({
        "message": "Egreso registrado",
        "total": total,
        "horas": horas
    })











#



from datetime import datetime
from config.db import db

class Egreso(db.Model):
    __tablename__ = "egresos"

    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, nullable=False)

    hora_salida = db.Column(db.DateTime, default=datetime.now)
    horas = db.Column(db.Integer)
    total = db.Column(db.Float)

    def serialize(self):
        return {
            "id": self.id,
            "vehiculo_id": self.vehiculo_id,
            "hora_salida": str(self.hora_salida),
            "horas": self.horas,
            "total": self.total
        }