##Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 4
class Factura:
    def __init__(self, importe: float, condicion: str):
        self.importe = importe
        self.condicion = condicion

    def mostrar(self):
        """Muestra los datos de la factura por consola."""
        print(f"Factura generada - Total: ${self.importe:.2f} - Condición: {self.condicion}")