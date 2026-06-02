from persona import Persona

class Profesor(Persona):
    def __init__(self, rut, nombre, email, especialidad):
        super().__init__(rut, nombre, email)
        self._especialidad = especialidad

    
    #polimorfismo

    def mostrar_datos(self):
        return f"Profesor: {self._nombre}, Epecialidad: {self._especialidad}"