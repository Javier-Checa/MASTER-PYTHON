"""
Ejercicio 6: Mostrar por consola todas las tablas de multiplicar en una sola ejecución del 1 al 10.

Se tendrá que mostrar primero el título de la tabla y luego las multiplicaciones mencionadas.  
   
"""

for cabecera in range(1,11):
    print("#############################################")
    print(f"############### Tabla del {cabecera} ###############")
    print("#############################################")
    
    for numero in range(1, 11):
        print(f"{numero} X {cabecera} = {numero*cabecera}")
        
    print("\n")
        
