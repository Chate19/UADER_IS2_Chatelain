#3. Represente la lista de piezas componentes de un ensamblado con sus
#relaciones jerárquicas. Empiece con un producto principal formado por tres
#sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases
#que representen esa configuración y la muestren. Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón
#composite).

class Componente:
    def mostrar(self, indent=0): pass

class Pieza(Componente):
    def __init__(self, nombre): self.nombre = nombre
    def mostrar(self, indent=0):
        print("  " * indent + f"- Pieza: {self.nombre}")

class Ensamblado(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []
    
    def agregar(self, componente): self.hijos.append(componente)
    
    def mostrar(self, indent=0):
        print("  " * indent + f"+ Conjunto: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(indent + 1)

# Estructura
producto_principal = Ensamblado("Producto Principal")
for i in range(1, 4):
    sub = Ensamblado(f"Sub-conjunto {i}")
    for j in range(1, 5):
        sub.agregar(Pieza(f"Pieza {i}.{j}"))
    producto_principal.agregar(sub)

producto_principal.mostrar()