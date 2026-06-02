from persona import Persona

class Alumno(Persona):
    def __init__(self, rut, nombre, email, matricula):
        super().__init__(rut, nombre, email)
        self._matricula = matricula
        self._evaluaciones = []
    
    def agregar_evaluacion(self, evaluacion):
        self._evaluaciones.append(evaluacion)

    # polimorfismo

    def mostrar_datos(self):
        return f"Alumno: {self._nombre}, Matricula: {self._matricula}"