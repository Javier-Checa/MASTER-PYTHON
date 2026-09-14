"""
Ejercicio 5: Crear una lista con el contenido de esta tabla: 

ACCION          AVENTURA            DEPORTES
GTA             ASSINS              FIFA 25
COD             CRASH               PES 25
PUGB            Prince of Persia    MOTO GP 25

Mostrar esta información ordenada.
"""

tabla = [
    {
        "categoria": "ACCIÓN",
        "juegos": ["GTA", "Call of Duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "Crash Bandicoot", "Prince of Persia"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 25", "PES 25", "MOTO GP 25"]
    }
]

for categoria in tabla:
        print(f"------------- {categoria['categoria']} -----------------")
        for juego in categoria['juegos']:
                print(juego)