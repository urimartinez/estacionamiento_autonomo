from flask import Blueprint
from models.cliente import Cliente
from config.db import db

# Creamos el Blueprint
cliente_bp = Blueprint("cliente_bp", __name__)

# Endpoint para listar clientes
@cliente_bp.route("/clientes", methods=["GET"])
def obtener_clientes():

    # Consulta todos los registros de la tabla cliente
    clientes = Cliente.query.all()

    # Convertimos cada objeto en diccionario JSON
    datos = [cliente.mostrarDatos() for cliente in clientes]

    return {
        "clientes": datos
    }