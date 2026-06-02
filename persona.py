class Persona:
    
    def __init__(self, rut, nombre, email):
        self._rut= rut
        self._nombre= nombre
        self._email= email

    def mostrar_datos(self):
        return f"Nombre: {self._nombre}, Email: {self._email} "
    