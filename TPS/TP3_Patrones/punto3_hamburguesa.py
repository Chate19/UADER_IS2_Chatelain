#Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 3
class Hamburguesa:
    def __init__(self, metodo: str):
        self.metodo = metodo

    def entregar(self):
        print(f"Hamburguesa lista. Método de entrega: {self.metodo}")