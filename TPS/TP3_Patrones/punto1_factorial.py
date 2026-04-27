#Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 1
class CalculadorFactorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadorFactorial, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n == 0: return 1
        return n * self.calcular(n - 1)