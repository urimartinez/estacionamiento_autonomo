from flask import Flask
from config.db import db
from dotenv import load_dotenv
import os

from models.cliente import Cliente
from models.espacio import Espacio
from models.tarifa import Tarifa

from routes.ruta_cliente import cliente_bp
from routes.ruta_espacio import espacio_bp
from routes.ruta_tarifa import tarifa_bp

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

db.init_app(app)

app.register_blueprint(cliente_bp)
app.register_blueprint(espacio_bp)
app.register_blueprint(tarifa_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
