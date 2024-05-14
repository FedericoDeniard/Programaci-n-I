class Personaje:

    # Constructor
    def __init__(self, nombre: str, nano: bool, vuela: bool,poder: str,pelea: int) -> None:
        self.nombre = nombre
        self.nanotecnologia = nano
        self.vuela = vuela
        self.super_poder = poder
        self.poder_pelea = pelea

    def presentarse(self) -> str:
        mensaje = f"{self.nombre} - {self.poder_pelea} - {self.super_poder} - "

        mensaje += "Usa nanotecnologia" if self.nanotecnologia else "No usa nanotecnologia"
        return mensaje
    
    def volar(self, altura, velocidad):
        if self.vuela:
            print(f"Estoy volando a {altura}m a una velodidad de {velocidad}km/h")
        else:
            print(f"{self.nombre} no puede volar")
    
    def atacar(self, enemigo: 'Personaje'):
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"{self.nombre} mató a {enemigo.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        elif self.poder_pelea < enemigo.poder_pelea:
            print(f"{enemigo.nombre} mató a {self.nombre}")
            enemigo.poder_pelea -= self.poder_pelea
            self.poder_pelea = 0
        else:
            print("Empataron")