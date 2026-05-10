from config.db import db

class Cliente(db.Model):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, nombre, email):

        self.nombre = nombre
        self.email = email

    def mostrarDatos(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }