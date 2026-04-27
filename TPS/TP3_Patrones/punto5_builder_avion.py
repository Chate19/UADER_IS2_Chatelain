#Trabajo Practico N°3 - Patrones de Diseño Creacionales - Chatelain Agustin

#Ejercicio 5
class Aircraft:
    """Clase Producto: Representa el objeto complejo a construir."""
    def __init__(self):
        self.parts = []

    def add_part(self, part: str):
        self.parts.append(part)

    def __str__(self):
        return f"Aeronave finalizada con: {', '.join(self.parts)}"


class AircraftBuilder:
    """Clase Builder: Contiene la lógica para construir las partes del avión."""
    def __init__(self):
        self._aircraft = Aircraft()

    def reset(self):
        self._aircraft = Aircraft()

    def build_body(self):
        self._aircraft.add_part("1 Fuselaje (Body)")

    def build_turbines(self):
        self._aircraft.add_part("2 Turbinas")

    def build_wings(self):
        self._aircraft.add_part("2 Alas")

    def build_landing_gear(self):
        self._aircraft.add_part("1 Tren de aterrizaje")

    def get_result(self) -> Aircraft:
        product = self._aircraft
        self.reset()  # Prepara el builder para una nueva construcción
        return product


class AerospaceDirector:
    """Clase Director: Define el orden de los pasos de construcción."""
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> AircraftBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: AircraftBuilder):
        self._builder = builder

    def construct_standard_plane(self):
        self.builder.build_body()
        self.builder.build_turbines()
        self.builder.build_wings()
        self.builder.build_landing_gear()