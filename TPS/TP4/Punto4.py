#4. Implemente una clase que permita a un número cualquiera imprimir su valor,
#luego agregarle sucesivamente.
#a. Sumarle 2.
#b. Multiplicarle por 2.
#c. Dividirlo por 3.
#mostrar los resultados de la clase sin agregados y con la invocación anidada a
#las clases con las diferentes operaciones. Use un patrón decorator para
#implementar

class Numero:
    def __init__(self, valor): self.valor = valor
    def get_valor(self): return self.valor

class OperacionDecorator(Numero):
    def __init__(self, numero): self.numero = numero

class SumarDos(OperacionDecorator):
    def get_valor(self): return self.numero.get_valor() + 2

class MultiplicarPorDos(OperacionDecorator):
    def get_valor(self): return self.numero.get_valor() * 2

class DividirPorTres(OperacionDecorator):
    def get_valor(self): return self.numero.get_valor() / 3

# Ejecución
n = Numero(10)
print(f"Original: {n.get_valor()}")

# Invocación anidada: ((10 + 2) * 2) / 3
anidado = DividirPorTres(MultiplicarPorDos(SumarDos(n)))
print(f"Decorado: {anidado.get_valor()}")