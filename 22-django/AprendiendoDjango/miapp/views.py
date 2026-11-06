from django.shortcuts import render, HttpResponse

# Crea tu vista aquí.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)

layout = """
<h1>Sitio Web con Django | Javier Checa</h1>
<hr/>
<ul>
    <li> 
        <a href="/inicio">Inicio</a> 
    </li>
    <li> 
        <a href="/hola-mundo">Hola Mundo</a> 
    </li>
    <li> 
        <a href="/tictactoe">Tic Tac Toe</a> 
    </li>
    <li> 
        <a href="/pagina">Página de pruebas</a> 
    </li>      
</ul>

"""

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
            if year % 2 == 0:           
                html += f"<li>{str(year)}</li>"
            year += 1
            
    html += "</ul>"
        
    return HttpResponse(html)

def tictactoe(request):
    # Ruta absoluta de tu archivo HTML del juego
    ruta_archivo = r"c:/wamp64/www/master-python/34-tictactoe/tres_en_raya_interactivo.html"
    
    try:
        # Abrimos y leemos el archivo HTML externo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido_html = archivo.read()
        return HttpResponse(contenido_html)
    except FileNotFoundError:
        return HttpResponse("<h1>Error: No se encontró el archivo del juego Tic Tac Toe en la ruta especificada.</h1>", status=404)

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
