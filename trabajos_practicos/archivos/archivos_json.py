# Javascript Object Notation
import json
from Data import *

def write_json():
    data = {}
    data["personas"] = []

    data["personas"].append({"nombre": "Juan","edad": 25})
    data["personas"].append({"nombre": "Benito","edad": 15})
    data["personas"].append({"nombre": "Maria","edad": 40})
    data["personas"].append({"nombre": "Luis","edad": 50})


    with open("trabajos_practicos/archivos/archivo.json","w") as file:
        json.dump(data, file,indent=2)

def read_json():
    with open("trabajos_practicos/archivos/archivo.json", "r") as file:
        data = json.load(file)
        print(data)

def generar_csv(path: str, data: list):
    with open(path, "w") as file:
        for song in data:
            cadena = f"{song['title']},{song['views']},{song['url']}\n"
            file.write(cadena)

#generar_csv('trabajos_practicos/archivos/playlist.csv',lista_bzrp)

import re
def parse_csv(path:str) -> list:
    lista = []
    with open(path,"r",encoding="utf8") as archivo:
        diccionario = {}
        for linea in archivo:
            valores = re.split(",|\n",linea)
            diccionario["title"] = valores[0]
            diccionario["views"] = valores[1]
            diccionario["url"] = valores[2]
            lista.append(diccionario)