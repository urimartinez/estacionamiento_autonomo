from datetime import datetime
from config.db import db

class Egreso(db.Model):
    __tablename__ = "Egresos"

    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, nullable=False)
    hora_salida = db.Column(db.DateTime, default=datetime.now)
    hora=db.Column(db.Integer)
    total = db.Column(db.Float)


    def serialize(self):
        return {
            "id": self.id,
            "vehiculo_id": self.vehiculo_id,
            "hora_salida": str(self.hora_salida),
            "hora":  self.hora,
            "total": self.total
        }
    



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