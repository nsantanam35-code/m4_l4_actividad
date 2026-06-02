
class Evaluacion:
    def __init__(self, nombre, nota): 
        self._nombre= nombre
        self._nota= nota

    #sobrecarga de metodos
    def calcular_resultado(self, exigencia=4.0):
        if self._nota >= exigencia:
            return "Aprobado"
        return"Reprobado"