#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    :param n: Número entero
    :return: Factorial de n
    :raises ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def main():
    """Punto de entrada del programa"""
    if len(sys.argv) < 2:
        print("Uso: python script.py <numero>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        sys.exit(1)

    try:
        result = factorial(num)
        print(f"El factorial de {num}! es {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

