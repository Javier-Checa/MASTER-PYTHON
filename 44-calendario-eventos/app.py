# app.py - Backend en Python con Flask y SQLite
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend HTML

DB_NAME = "calendar.db"

# Inicializar Base de Datos SQLite
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT,
                color TEXT DEFAULT 'indigo',
                desc TEXT
            )
        ''')
        conn.commit()

init_db()

# REST API ENDPOINTS

# 1. Obtener todos los eventos
@app.route('/api/events', methods=['GET'])
def get_events():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, date, time, color, desc FROM events")
        rows = cursor.fetchall()
        events = [
            {"id": row[0], "title": row[1], "date": row[2], "time": row[3], "color": row[4], "desc": row[5]}
            for row in rows
        ]
        return jsonify(events)

# 2. Crear un evento nuevo
@app.route('/api/events', methods=['POST'])
def create_event():
    data = request.json
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO events (title, date, time, color, desc) VALUES (?, ?, ?, ?, ?)",
            (data['title'], data['date'], data.get('time'), data.get('color', 'indigo'), data.get('desc'))
        )
        conn.commit()
        return jsonify({"message": "Evento creado", "id": cursor.lastrowid}), 201

# 3. Eliminar un evento por ID
@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
        conn.commit()
        return jsonify({"message": "Evento eliminado"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)