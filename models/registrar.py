from config.db import db
class registro_vehiculo(db.Model):
    _tablename_ ="registro_vehiculo"
    id=db.Column(db.integer,primary_key=True)