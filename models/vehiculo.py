class vehiculo:
    def __init__(self,patente,modelo,marca,año):
        self.patente=patente
        self.modelo=modelo
        self.marca=marca
        self.año=año

    def mostrar_vehiculo(self):
        return f"patente: {self.patente}, modelo: {self.modelo}, marca: {self.marca}, año: {self.año}"
    