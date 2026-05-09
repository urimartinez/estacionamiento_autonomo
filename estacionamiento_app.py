from dotenv import load_dotenv
import os
from flask import Flask
from config.db import db
from models import Vehiculo
from routes.vehiculo_r import vehiculo_bp
from routes.ingreso_r import ingreso_bp
from models import registrar

load_dotenv()
app = Flask(__name__)


user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD") or ""
host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")

uri = f"mysql+pymysql://{user}:{password}@{host}/{dbname}"

app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) 
#rutas:
app.register_blueprint(vehiculo_bp)
app.register_blueprint(ingreso_bp)
app.register_blueprint(registrar_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)