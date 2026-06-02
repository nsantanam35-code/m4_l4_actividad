
class Curso:
    def __init__(self, nombre, anio):
        self._nombre= nombre
        self._anio= anio
        self._asignaturas = []

    def agregar_asignatura(self, asignatura):
        self._asignaturas.append(asignatura)