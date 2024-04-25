'''
Nombre: Federico
Apellido: Deniard
'''

def get_discount (price: int, discount:int) -> int | float:
    total = price - ((price * discount) / 100)
    return total

x = get_discount(100, 0)
print(x)