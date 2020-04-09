from enum import IntEnum

class EstadoTruco(IntEnum):
    nosecanto = 1
    truco = 2
    retruco = 3
    valecuatro = 4


inicial = EstadoTruco.nosecanto
seEstaCantando = EstadoTruco(inicial + 1)  
print(seEstaCantando.name)