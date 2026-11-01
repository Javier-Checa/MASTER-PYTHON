from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Lista en memoria para almacenar los registros durante la ejecución
personas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/personas', methods=['GET'])
def obtener_personas():
    return jsonify(personas)

@app.route('/api/personas', methods=['POST'])
def agregar_persona():
    datos = request.get_json()
    
    # Validar que los campos requeridos existan
    if not datos or not datos.get('nombre'):
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    nueva_persona = {
        'nombre': datos.get('nombre', ''),
        'direccion': datos.get('direccion', ''),
        'telefono': datos.get('telefono', ''),
        'email': datos.get('email', ''),
        'notas': datos.get('notas', '')
    }
    
    personas.append(nueva_persona)
    return jsonify({'mensaje': 'Persona agregada correctamente', 'persona': nueva_persona}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)