from class_personaje import *

def mostrar_lista_personaje(lista: list[Personaje]):
    for heroe in lista_heroes:
        print(heroe.presentarse())

# def mostrar(heroe: Personaje):
#     print(f"{heroe.nombre} - {heroe.super_poder} - {heroe.poder_pelea}")

spiderman = Personaje("Spiderman", True, False,"Telaraña",800)
ironman = Personaje("Iron-Man",True,True,"Disparo ultrasonico",1500)
hulk = Personaje("Hulk",False,False,"Aplastar",1200)
deadpool = Personaje("Deadpool",False,False,"Espadas",750)

# mostrar(ironman)
# print(spiderman.presentarse())
# spiderman.volar(500,250)
# ironman.volar(100,50)
# spiderman.atacar(ironman)

lista_heroes: list[Personaje] = []

lista_heroes.append(ironman)
lista_heroes.append(spiderman)
lista_heroes.append(hulk)
lista_heroes.append(deadpool)

mostrar_lista_personaje(lista_heroes)