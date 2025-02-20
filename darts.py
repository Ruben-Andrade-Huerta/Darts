import math

def score(x, y):
    distancia = math.sqrt(x**2 + y**2)
    if distancia <= 1:
        return 10
    elif distancia <= 5 and distancia > 1:
        return 5
    elif distancia <= 10 and distancia > 5:
        return 1
    else:
        return 0
