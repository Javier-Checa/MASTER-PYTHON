"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, solo están disponibles denytro, a 
no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función
y están disponibles dentro y fuera de ellas.    
"""

# Variable global
frase = "\nNi los genios son tan genios, ni los mediocres tan mediocres.\n"

print(frase)


# Variable local
def holaMundo():

    frase = "\nHola mundo, soy una variable local.\n"
    print("Dentro de la función: ")
    print(frase)

    year = 2026
    print("Dentro de la función: ")
    print(year)

    global website  # Indicamos que vamos a usar la variable global
    website = "javierchecapage.com"
    print("DENTRO: ", website)
    print(website)

    return "Dato devuelto: " + str(year) + " - Website: " + website



print(holaMundo())
print("FUERA: ", website)

    

