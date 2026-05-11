from flask import Flask
from dotenv import load_dotenv
from config.db import db
import os

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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)