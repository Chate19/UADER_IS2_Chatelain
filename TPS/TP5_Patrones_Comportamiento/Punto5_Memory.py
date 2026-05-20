import os

#*--------------------------------------------------------------------
#* Punto 5: IS2_taller_memory.py modificado
#* La clase Radio almacena hasta 4 estados anteriores.
#* El método undo(pasos) acepta:
#*   0 -> recupera el inmediato anterior
#*   1 -> recupera el anterior a ese (2 pasos atrás)
#*   2 -> 3 pasos atrás
#*   3 -> 4 pasos atrás (el más antiguo guardado)
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

    def __init__(self, radio):
        self.radio    = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos      = 0
        self.name     = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):

    def __init__(self, radio):
        self.radio    = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos      = 0
        self.name     = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


#*--------------------------------------------------------------------
#* Snapshot: guarda una "foto" del estado de la radio en un momento
#*--------------------------------------------------------------------
class Snapshot:
    """Almacena el estado (banda y posición) de la radio."""

    def __init__(self, banda, pos):
        self.banda = banda   # 'AM' o 'FM'
        self.pos   = pos     # posición en la lista de estaciones

    def __repr__(self):
        return f"Snapshot(banda={self.banda}, pos={self.pos})"


#*--------------------------------------------------------------------
#* Radio con historial de hasta 4 estados y undo(pasos)
#*--------------------------------------------------------------------
class Radio:

    MAX_HISTORIAL = 4

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state   = self.fmstate

        # Historial de snapshots (el último es el más reciente)
        self._historial = []

    # ----------------------------------------------------------------
    # Guardar estado actual en el historial
    # ----------------------------------------------------------------
    def _guardar_snapshot(self):
        banda = self.state.name
        pos   = self.state.pos
        snap  = Snapshot(banda, pos)
        self._historial.append(snap)
        # Mantener máximo MAX_HISTORIAL entradas
        if len(self._historial) > self.MAX_HISTORIAL:
            self._historial.pop(0)
        print(f"  [Historial guardado] {snap}  "
              f"(total en historial: {len(self._historial)})")

    # ----------------------------------------------------------------
    # Restaurar un snapshot en la radio
    # ----------------------------------------------------------------
    def _restaurar_snapshot(self, snap):
        if snap.banda == "AM":
            self.state = self.amstate
            self.state.pos = snap.pos
        else:
            self.state = self.fmstate
            self.state.pos = snap.pos
        print(f"  [Restaurado] Banda={self.state.name}, "
              f"Estación={self.state.stations[self.state.pos]}")

    # ----------------------------------------------------------------
    # Acciones públicas
    # ----------------------------------------------------------------
    def toggle_amfm(self):
        self._guardar_snapshot()
        self.state.toggle_amfm()

    def scan(self):
        self._guardar_snapshot()
        self.state.scan()

    # ----------------------------------------------------------------
    # undo(pasos):
    #   pasos=0 -> inmediato anterior   (historial[-1])
    #   pasos=1 -> 2 pasos atrás        (historial[-2])
    #   pasos=2 -> 3 pasos atrás        (historial[-3])
    #   pasos=3 -> 4 pasos atrás        (historial[-4])
    # ----------------------------------------------------------------
    def undo(self, pasos=0):
        if pasos not in (0, 1, 2, 3):
            print("  [UNDO] Argumento inválido. Use 0, 1, 2 o 3.")
            return

        indice = -(pasos + 1)   # -1, -2, -3 o -4
        if abs(indice) > len(self._historial):
            print(f"  [UNDO] No hay suficientes estados en el historial "
                  f"(pedido={pasos+1}, disponibles={len(self._historial)})")
            return

        snap = self._historial[indice]
        print(f"\n  [UNDO pasos={pasos}] Recuperando {snap}")
        self._restaurar_snapshot(snap)

        # Opcional: eliminar los estados posteriores al restaurado
        self._historial = self._historial[:len(self._historial) + indice]


#*---------------------
if __name__ == "__main__":
    os.system("clear")
    print("=" * 60)
    print("  Patrón: State + Memento (historial de estados)")
    print("  undo(0)=anterior, undo(1)=2 atrás, undo(2)=3, undo(3)=4")
    print("=" * 60)

    radio = Radio()

    print("\n--- Realizando acciones ---\n")
    radio.scan()          # Estado 1 guardado
    radio.scan()          # Estado 2 guardado
    radio.toggle_amfm()   # Estado 3 guardado -> cambia a AM
    radio.scan()          # Estado 4 guardado
    radio.scan()          # Estado 5 -> guarda, descarta el más viejo

    print(f"\nEstado actual: {radio.state.name}, "
          f"estación: {radio.state.stations[radio.state.pos]}")

    print("\n--- Probando undo ---\n")

    print("undo(0) -> recupera el inmediato anterior:")
    radio.undo(0)

    print("\nundo(1) -> recupera 2 estados atrás:")
    radio.undo(1)

    print("\nundo(2) -> recupera 3 estados atrás:")
    radio.undo(2)

    print("\nundo(3) -> recupera 4 estados atrás:")
    radio.undo(3)

    print("\nundo(3) de nuevo -> historial insuficiente:")
    radio.undo(3)

    print("\n" + "=" * 60)