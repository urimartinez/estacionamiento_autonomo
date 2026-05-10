from config.db import db

class Tarifa(db.Model):

    __tablename__ = "tarifas"

    id = db.Column(db.Integer, primary_key=True)

    descripcion = db.Column(
        db.String(50),
        nullable=False
    )

    precio_hora = db.Column(
        db.Float,
        nullable=False
    )

    def __init__(self, descripcion, precio_hora):

        self.descripcion = descripcion
        self.precio_hora = precio_hora

    def serialize(self):

        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio_hora": self.precio_hora
        }