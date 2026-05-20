import os

#*--------------------------------------------------------------------
#* Punto 1: Patrón Cadena de Responsabilidad
#* Los números del 1 al 100 se pasan en secuencia.
#* - PrimeHandler: consume números primos
#* - EvenHandler: consume números pares
#* - Si ninguno lo consume, se marca como no consumido
#*--------------------------------------------------------------------

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class Handler:
    """Clase base del handler en la cadena."""

    def __init__(self):
        self._siguiente = None

    def set_siguiente(self, handler):
        self._siguiente = handler
        return handler  # Permite encadenamiento fluido

    def manejar(self, numero):
        if self._siguiente:
            return self._siguiente.manejar(numero)
        # Ningún handler lo consumió
        print(f"  Número {numero}: NO CONSUMIDO")
        return False


class PrimeHandler(Handler):
    """Consume números primos."""

    def manejar(self, numero):
        if es_primo(numero):
            print(f"  Número {numero}: consumido por PrimeHandler (primo)")
            return True
        return super().manejar(numero)


class EvenHandler(Handler):
    """Consume números pares (no primos, ya que los primos fueron antes)."""

    def manejar(self, numero):
        if numero % 2 == 0:
            print(f"  Número {numero}: consumido por EvenHandler (par)")
            return True
        return super().manejar(numero)


#*---------------------
if __name__ == "__main__":
    os.system("clear")
    print("=" * 60)
    print("  Patrón: Cadena de Responsabilidad")
    print("  Números del 1 al 100")
    print("=" * 60)

    # Construir la cadena: Primo -> Par -> (no consumido)
    prime_handler = PrimeHandler()
    even_handler  = EvenHandler()
    prime_handler.set_siguiente(even_handler)

    print("\nProcesando números del 1 al 100:\n")
    for numero in range(1, 101):
        prime_handler.manejar(numero)

    print("\n" + "=" * 60)
    print("Resumen de la cadena:")
    print("  1° PrimeHandler -> consume primos")
    print("  2° EvenHandler  -> consume pares restantes")
    print("  Sin handler     -> marcado como NO CONSUMIDO")
    print("=" * 60)