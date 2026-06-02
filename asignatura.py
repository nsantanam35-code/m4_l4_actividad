
class Asignatura:
    def __init__(self, codigo, nombre, creditos):
        self._codigo= codigo
        self._nombre= nombre
        self._creditos= creditos
        self._evaluaciones = []

    def agregar_evaluacion(self, evaluacion):
        self._evaluaciones.append(evaluacion)