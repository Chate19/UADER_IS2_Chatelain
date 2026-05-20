import os
import random
import string

#*--------------------------------------------------------------------
#* Punto 3: Patrón Observer
#* - Un emisor emite IDs de 4 caracteres.
#* - 4 clases subscriptas, cada una con su propio ID fijo.
#* - Cuando el ID emitido coincide con el ID del observer,
#*   éste imprime un mensaje.
#* - Se emiten 8 IDs, al menos 4 deben coincidir con algún observer.
#*--------------------------------------------------------------------

class Emisor:
    """Sujeto observable. Emite IDs y notifica a los observers."""

    def __init__(self):
        self._observers = []

    def suscribir(self, observer):
        self._observers.append(observer)

    def desuscribir(self, observer):
        self._observers.remove(observer)

    def emitir(self, id_emitido):
        print(f"\n[EMISOR] ID emitido: '{id_emitido}'")
        for observer in self._observers:
            observer.actualizar(id_emitido)


class ObserverBase:
    """Clase base para todos los observers."""

    def __init__(self, nombre, id_propio):
        self.nombre   = nombre
        self.id_propio = id_propio

    def actualizar(self, id_emitido):
        if id_emitido == self.id_propio:
            print(f"  ✔ [{self.nombre}] ¡Coincidencia! "
                  f"ID emitido '{id_emitido}' == mi ID '{self.id_propio}'")
        else:
            print(f"  ✘ [{self.nombre}] Sin coincidencia "
                  f"(emitido='{id_emitido}', mío='{self.id_propio}')")


class ObserverAlfa(ObserverBase):
    def __init__(self):
        super().__init__("ObserverAlfa", "AB12")


class ObserverBeta(ObserverBase):
    def __init__(self):
        super().__init__("ObserverBeta", "CD34")


class ObserverGamma(ObserverBase):
    def __init__(self):
        super().__init__("ObserverGamma", "EF56")


class ObserverDelta(ObserverBase):
    def __init__(self):
        super().__init__("ObserverDelta", "GH78")


#*---------------------
if __name__ == "__main__":
    os.system("clear")
    print("=" * 60)
    print("  Patrón: Observer")
    print("  IDs de 4 caracteres, 8 emisiones")
    print("=" * 60)

    # Crear sujeto y observers
    emisor = Emisor()
    alfa   = ObserverAlfa()
    beta   = ObserverBeta()
    gamma  = ObserverGamma()
    delta  = ObserverDelta()

    # Suscribir los 4 observers
    for obs in [alfa, beta, gamma, delta]:
        emisor.suscribir(obs)

    ids_conocidos = [alfa.id_propio, beta.id_propio,
                     gamma.id_propio, delta.id_propio]

    print(f"\nIDs registrados en los observers: {ids_conocidos}")

    # Generar 8 IDs: garantizamos al menos 4 coincidencias
    # tomando los 4 IDs conocidos + 4 aleatorios
    def id_aleatorio():
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choices(chars, k=4))

    # 4 IDs que coinciden (mezclados) + 4 aleatorios
    ids_a_emitir = ids_conocidos.copy()
    for _ in range(4):
        ids_a_emitir.append(id_aleatorio())

    random.shuffle(ids_a_emitir)

    print(f"IDs que se emitirán: {ids_a_emitir}\n")
    print("-" * 60)

    coincidencias = 0
    for id_emitido in ids_a_emitir:
        emisor.emitir(id_emitido)
        if id_emitido in ids_conocidos:
            coincidencias += 1

    print("\n" + "=" * 60)
    print(f"Total de coincidencias: {coincidencias} / {len(ids_a_emitir)}")
    print("=" * 60)