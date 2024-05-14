'''
Metodos de lista

append: Me permite agragar un elemento al final de la lista. (value)
insert: Agrega un elemento en una posición específica. Los elementos que se encuentran después del insertado, se mueven de índice hacia la derecha. (index, value)
remove: Elimina la primera ocurrencia del valor que le pasamos. (value) Para eliminar todas, hago for each
pop: Devuelve el elemento que elimino. (index)
index: Devuelve el índice de la primera ocurrencia. (value)
sort: Ordena la lista.
reverse: Ordena la lista del final al inicio.
clear: Elimina todos los elementos de la lista.
count: Devuelve cuantas veces aparece un elemento en la lista.
'''

lista = [7,3,6]             # 7 3 6
lista.append(5)             # 7 3 6 5
lista.insert(1,1)           # 7 1 3 6 5
lista.remove(3)             # 7 1 6 5
elemento = lista.pop(2)     # 6                 # 7 1 5
lista.sort()                # 1 5 7
print(elemento)             
print(lista)