#2. Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho
#dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro
#de 10 mts. Genere una clase que represente a las láminas en forma genérica al
#cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el
#patrón bridge en la solución).

# Implementador (Interfaz de Trenes)
class TrenLaminador:
    def laminar(self): pass

class Tren5Meters(TrenLaminador):
    def laminar(self): return "Produciendo plancha de 5 mts"

class Tren10Meters(TrenLaminador):
    def laminar(self): return "Produciendo plancha de 10 mts"

# Abstracción (La Lámina)
class LaminaAcero:
    def __init__(self, tren: TrenLaminador):
        self.tren = tren
        self.espesor = "0.5\""
        self.ancho = "1.5 mts"

    def producir(self):
        print(f"Lámina {self.espesor}x{self.ancho} -> {self.tren.laminar()}")

# Uso
lamina1 = LaminaAcero(Tren5Meters())
lamina1.producir()