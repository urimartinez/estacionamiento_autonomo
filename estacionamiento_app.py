from flask import Flask
from dotenv import load_dotenv
import os

from config.db import db

from models.vehiculo import Vehiculo
from models.ingreso import Ingreso
from models.egreso import Egreso



from routes.vehiculo_r import vehiculo_bp
from routes.ingreso_r import ingreso_bp
from routes.egreso_r import egreso_bp


load_dotenv()

app = Flask(__name__)

# Configuración de base de datos
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD") or ""
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{user}:{password}@{host}/{dbname}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar DB
db.init_app(app)

# Registrar rutas
app.register_blueprint(vehiculo_bp)
app.register_blueprint(ingreso_bp)
app.register_blueprint(egreso_bp)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)