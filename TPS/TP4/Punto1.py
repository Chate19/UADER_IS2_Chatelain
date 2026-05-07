#1. Provea una clase ping que luego de creada al ser invocada con un método
#“execute(string)” realice 10 intentos de ping a la dirección IP contenida en
#“string” (argumento pasado), la clase solo debe funcionar si la dirección IP
#provista comienza con “192.”. Provea un método executefree(string) que haga
#lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy
#cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a
#www.google.com usando el método executefree de ping y re-envie a execute
#de la clase ping en cualquier otro caso. (Modele la solución como un patrón
#proxy).

class Ping:
    def execute(self, ip):
        if ip.startswith("192."):
            print(f"Ping (controlado) a {ip}: Realizando 10 intentos...")
        else:
            print("Error: La dirección IP no comienza con 192.")

    def executefree(self, ip):
        print(f"Ping (libre) a {ip}: Realizando 10 intentos...")

class PingProxy:
    def __init__(self):
        self.ping_real = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            print("Proxy: Redireccionando caso especial...")
            self.ping_real.executefree("www.google.com")
        else:
            self.ping_real.execute(ip)