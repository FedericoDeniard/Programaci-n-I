from class_boligrafo import *

bic = Boligrafo("fino", "rojo")
paper_mate = Boligrafo("grueso", "azul")

print(bic.obtener_propiedades())
print(paper_mate.obtener_propiedades())
print("--------------------------------------")
bic.escribir("El gato saltó sobre el muro alto. Y no tuvo ninguna lesión")
paper_mate.escribir("El gato saltó sobre el muro alto. Y no tuvo ninguna lesión")
print("--------------------------------------")
print(bic.obtener_propiedades())
print(paper_mate.obtener_propiedades())
