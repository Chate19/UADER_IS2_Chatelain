import os

#*--------------------------------------------------------------------
#* Punto 4: IS2_taller_scanner.py modificado
#* Agrega memorias M1, M2, M3, M4 que pueden ser AM o FM.
#* En cada ciclo de barrido se barren también las 4 memorias.
#*--------------------------------------------------------------------

class State:
    """Clase base de estado."""

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(
            self.stations[self.pos], self.name))


class AmState(State):
    """Estado AM: barre estaciones de AM."""

    def __init__(self, radio):
        self.radio    = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos      = 0
        self.name     = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    """Estado FM: barre estaciones de FM."""

    def __init__(self, radio):
        self.radio    = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos      = 0
        self.name     = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


#*--------------------------------------------------------------------
#* Clase Memoria: representa una memoria M1-M4
#* Cada memoria tiene una banda (AM/FM) y una frecuencia específica.
#*--------------------------------------------------------------------
class Memoria:

    def __init__(self, etiqueta, banda, frecuencia):
        """
        etiqueta  : 'M1', 'M2', 'M3', 'M4'
        banda     : 'AM' o 'FM'
        frecuencia: string con la frecuencia (ej. '103.9' o '1250')
        """
        self.etiqueta   = etiqueta
        self.banda      = banda
        self.frecuencia = frecuencia

    def sintonizar(self):
        print(f"  [{self.etiqueta}] Memoria -> Estación {self.frecuencia} {self.banda}")


#*--------------------------------------------------------------------
#* Radio modificada con soporte de memorias M1-M4
#*--------------------------------------------------------------------
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        # Inicialmente en FM
        self.state = self.fmstate

        # Memorias predefinidas: 2 AM + 2 FM (pueden ser cualquier combo)
        self.memorias = [
            Memoria("M1", "AM", "1250"),
            Memoria("M2", "FM", "89.1"),
            Memoria("M3", "AM", "1510"),
            Memoria("M4", "FM", "103.9"),
        ]

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def scan_memorias(self):
        """Barre las cuatro memorias en orden."""
        print("  -- Barriendo memorias --")
        for memoria in self.memorias:
            memoria.sintonizar()
        print("  -- Fin memorias --")


#*---------------------
if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()

    # Acciones originales: 3 scan + toggle + 3 scan, repetido 2 veces
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Memorias configuradas:")
    for m in radio.memorias:
        print(f"  {m.etiqueta}: {m.frecuencia} {m.banda}")

    print("\nRecorre las acciones ejecutando la acción, "
          "el objeto cambia la interfaz según el estado.")
    print("En cada ciclo de barrido también se barren las 4 memorias.\n")

    ciclo = 0
    for action in actions:
        action()
        # Después de cada scan (no del toggle) se barren las memorias
        if action == radio.scan:
            ciclo += 1
            if ciclo % 3 == 0:  # Al completar un bloque de 3 scans
                radio.scan_memorias()