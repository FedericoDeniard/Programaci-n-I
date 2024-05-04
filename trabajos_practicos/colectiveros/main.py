from random import *
from Packages.Package_Input.Input import *

drivers = 15
drivers_id = [[0] for _ in range(drivers)]


def create_id(ids: list) -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    id = ""
    for i in range(5):
        id += letters[randint(0, 25)]

    for j in range(5):
        id += str(randint(0, 9))
    
    
    for k in range(len(ids)):
        if id == ids[k]:
            id = create_id(ids)

    return id

def main():
    for i in range(drivers):
        drivers_id[i] = create_id(drivers_id)
    id = get_string("Ingrese su numero de legajo: ",10,10)
    print(f"Tu id es: {id}")
main()

