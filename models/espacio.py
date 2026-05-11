from config.db import db
class Espacio(db.Model):

    __tablename__ = "espacios"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer,unique=True,nullable=False)
    ocupado = db.Column( db.Boolean,default=False)

    def __init__(self, numero):
        self.numero = numero

    def serialize(self):

        return {
            "id": self.id,
            "numero": self.numero,
            "ocupado": self.ocupado
        }