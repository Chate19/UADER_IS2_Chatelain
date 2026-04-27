#Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 2
class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total(self, base: float) -> float:
        iva = base * 0.21
        iibb = base * 0.05
        muni = base * 0.012
        return base + iva + iibb + muni