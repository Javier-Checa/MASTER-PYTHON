from django.shortcuts import render, HttpResponse

# Crea tu vista aquí.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)

def index(request):
    
    html = """
        <h1>Proyecto Web con Django</h1>
        <p>Creado por Javier Checa</p>
        <p>Estamos en la ruta: <strong>/</strong></p>
        <br>
        <p> Años hasta el 2050: </p>
        <ul>
    """
    year = 2026
        
    while year <= 2050:
            html += f"<li>{str(year)}</li>"
            year += 1
            
    html += "</ul>"
        
    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("""
        <h1>¡Hola, Mundo, con Django!</h1>
        <p>Este es mi primer proyecto con Django</p>
        <p>Estamos en la ruta: <strong>/hola-mundo/</strong></p>""")
    
def pagina(request):
    return HttpResponse("""
        <h1>Página de mi sitio web</h1>
        <p>Creada por Javier Checa</p>
    """)   
