"""
Los paquetes son conjuntos de módulos de Python agrupados
"""

print("PROBANDO PAQUETES: ")

from mipaquete import pruebas
from mipaquete import herramientas

# También se pueden importar los módulos conjuntamente: 
# from mipaquete import pruebas, herramientas


pruebas.probando()
herramientas.nombreCompleto("Javier", "Checa")