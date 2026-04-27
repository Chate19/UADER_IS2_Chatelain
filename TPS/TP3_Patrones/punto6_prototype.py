#Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 6
import copy

class Prototype:
    """
    Clase que implementa la capacidad de clonarse.
    Se utiliza copy.deepcopy para asegurar que los objetos anidados también se copien.
    """
    def __init__(self, identifier: str, data: list):
        self.identifier = identifier
        self.data = data

    def clone(self):
        # El método deepcopy garantiza que no queden referencias al objeto original
        return copy.deepcopy(self)

    def __str__(self):
        return f"Prototipo [{self.identifier}] - Datos: {self.data}"

# Verificación de que un clon puede generar otro clon
if __name__ == "__main__":
    # 1. Creamos el original
    original = Prototype("P-Original", [10, 20, 30])
    
    # 2. Generamos la primera copia desde el original
    copia_1 = original.clone()
    copia_1.identifier = "P-Copia-1"
    
    # 3. Verificamos que la copia puede generar otra copia de sí misma
    copia_2 = copia_1.clone()
    copia_2.identifier = "P-Copia-2"
    
    print(original)
    print(copia_1)
    print(copia_2)