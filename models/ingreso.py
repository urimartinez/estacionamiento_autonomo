from datetime import datetime
from config.db import db

class Ingreso(db.Model):
    __tablename__ = "ingresos"

    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, nullable=False)
    hora_ingreso = db.Column(db.DateTime, default=datetime.now)

    def serialize(self):
        return {
            "id": self.id,
            "vehiculo_id": self.vehiculo_id,
            "hora_ingreso": str(self.hora_ingreso)
        }