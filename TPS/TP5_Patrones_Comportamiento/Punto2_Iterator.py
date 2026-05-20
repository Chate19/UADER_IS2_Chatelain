import os

#*--------------------------------------------------------------------
#* Punto 2: Patrón Iterator
#* Almacena una cadena de caracteres y permite recorrerla
#* en sentido directo y reverso.
#*--------------------------------------------------------------------

class StringIterator:
    """Iterador directo sobre una cadena de caracteres."""

    def __init__(self, cadena):
        self._cadena = cadena
        self._indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice >= len(self._cadena):
            raise StopIteration
        caracter = self._cadena[self._indice]
        self._indice += 1
        return caracter

    def reset(self):
        self._indice = 0


class StringReverseIterator:
    """Iterador inverso sobre una cadena de caracteres."""

    def __init__(self, cadena):
        self._cadena = cadena
        self._indice = len(cadena) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < 0:
            raise StopIteration
        caracter = self._cadena[self._indice]
        self._indice -= 1
        return caracter

    def reset(self):
        self._indice = len(self._cadena) - 1


class CadenaIterable:
    """
    Colección que almacena una cadena de caracteres
    y provee iteradores directo y reverso.
    """

    def __init__(self, cadena):
        self._cadena = cadena

    def __iter__(self):
        """Iterador directo por defecto."""
        return StringIterator(self._cadena)

    def iter_reverso(self):
        """Devuelve un iterador en sentido inverso."""
        return StringReverseIterator(self._cadena)

    def __len__(self):
        return len(self._cadena)

    def __str__(self):
        return self._cadena


#*---------------------
if __name__ == "__main__":
    os.system("clear")
    print("=" * 60)
    print("  Patrón: Iterator")
    print("  Recorrido directo y reverso de una cadena")
    print("=" * 60)

    cadena = CadenaIterable("Hola Mundo!")

    print(f"\nCadena original: '{cadena}'")
    print(f"Longitud: {len(cadena)}\n")

    # Recorrido directo
    print("Recorrido DIRECTO (carácter por carácter):")
    for char in cadena:
        print(f"  -> '{char}'")

    # Recorrido reverso
    print("\nRecorrido REVERSO (carácter por carácter):")
    for char in cadena.iter_reverso():
        print(f"  -> '{char}'")

    # Reconstruir la cadena en ambos sentidos
    directa  = "".join(c for c in cadena)
    inversa  = "".join(c for c in cadena.iter_reverso())
    print(f"\nCadena directa reconstruida : '{directa}'")
    print(f"Cadena inversa reconstruida : '{inversa}'")
    print("=" * 60)