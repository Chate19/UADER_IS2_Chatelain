# main.py
from punto1_factorial import CalculadorFactorial
from punto2_impuestos import CalculadoraImpuestos
from punto3_hamburguesa import Hamburguesa
from punto4_factura import Factura
from punto5_builder_avion import AerospaceDirector, AircraftBuilder
from punto6_prototype import Prototype

def ejecutar_tp():
    print("=== TRABAJO PRÁCTICO 3: PATRONES DE CREACIÓN ===")
    print(f"{'='*48}\n")

    # PUNTO 1
    print("PUNTO 1: Singleton Factorial")
    f1 = CalculadorFactorial()
    f2 = CalculadorFactorial()
    print(f"¿Es la misma instancia? {f1 is f2}")
    print(f"Resultado factorial de 5: {f1.calcular(5)}\n")

    # PUNTO 2
    print("PUNTO 2: Singleton Impuestos")
    tax = CalculadoraImpuestos()
    print(f"Total con impuestos (Base 1000): ${tax.calcular_total(1000)}\n")

    # PUNTO 3
    print("PUNTO 3: Factory Hamburguesa")
    h1 = Hamburguesa("Mostrador")
    h2 = Hamburguesa("Delivery")
    h1.entregar()
    h2.entregar()
    print("\n")

    # PUNTO 4
    print("PUNTO 4: Factura según Condición")
    fact = Factura(5500.50, "IVA Responsable Inscripto")
    fact.mostrar()
    print("\n")

    # PUNTO 5
    print("PUNTO 5: Builder Avión")
    director = AerospaceDirector()
    builder = AircraftBuilder()
    director.builder = builder
    director.construct_standard_plane()
    print(builder.get_result())
    print("\n")

    # PUNTO 6
    print("PUNTO 6: Prototype")
    p1 = Prototype("Prototipo-Base", [1, 2, 3])
    p2 = p1.clone()
    p3 = p2.clone()
    print(f"Original: {p1}")
    print(f"Clon del clon: {p3}\n")

    # PUNTO 7
    print("PUNTO 7: Abstract Factory")
    print("Análisis teórico incluido en la memoria técnica adjunta.")

if __name__ == "__main__":
    ejecutar_tp()