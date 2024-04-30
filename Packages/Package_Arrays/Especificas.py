def check_parity(number: int)->bool:
    parity = False
    if number % 2 == 0:
        parity = True
    return parity

def check_positive(number: int)->bool:
    positive = None
    if number > 0:
        positive = True
    elif number < 0:
        positive = False
    return positive