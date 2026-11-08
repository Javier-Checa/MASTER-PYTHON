import sqlite3
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
DB_NAME = "consultorio.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tabla Especialidades
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS especialidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """
    )

    # Insertar las 6 especialidades requeridas si no existen
    especialidades_iniciales = [
        "Traumatología",
        "Pediatría",
        "Nefrología",
        "Medicina Familiar",
        "Odontología",
        "Ginecología",
    ]
    for esp in especialidades_iniciales:
        cursor.execute(
            "INSERT OR IGNORE INTO especialidades (nombre) VALUES (?)", (esp,)
        )

    # Tabla Médicos / Profesionales
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especialidad_id INTEGER NOT NULL,
            telefono TEXT,
            email TEXT,
            FOREIGN KEY (especialidad_id) REFERENCES especialidades (id)
        )
    """
    )

    # Tabla Pacientes
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            documento TEXT UNIQUE NOT NULL,
            telefono TEXT,
            email TEXT,
            fecha_nacimiento TEXT
        )
    """
    )

    # Tabla Citas
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            paciente_id INTEGER NOT NULL,
            medico_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            motivo TEXT,
            estado TEXT DEFAULT 'Programada',
            FOREIGN KEY (paciente_id) REFERENCES pacientes (id) ON DELETE CASCADE,
            FOREIGN KEY (medico_id) REFERENCES medicos (id) ON DELETE CASCADE
        )
    """
    )

    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# ENDPOINTS API REST (CRUD)
# ==========================================


# --- ESPECIALIDADES ---
@app.route("/api/especialidades", methods=["GET"])
def get_especialidades():
    conn = get_db_connection()
    items = conn.execute("SELECT * FROM especialidades").fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])


# --- MÉDICOS ---
@app.route("/api/medicos", methods=["GET", "POST"])
def manage_medicos():
    conn = get_db_connection()

    if request.method == "POST":
        data = request.json
        conn.execute(
            "INSERT INTO medicos (nombre, especialidad_id, telefono, email) VALUES (?, ?, ?, ?)",
            (
                data["nombre"],
                data["especialidad_id"],
                data.get("telefono"),
                data.get("email"),
            ),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Médico agregado exitosamente"}), 201

    query = """
        SELECT m.id, m.nombre, m.telefono, m.email, m.especialidad_id, e.nombre as especialidad 
        FROM medicos m 
        JOIN especialidades e ON m.especialidad_id = e.id
    """
    items = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])


@app.route("/api/medicos/<int:id>", methods=["PUT", "DELETE"])
def update_delete_medico(id):
    conn = get_db_connection()

    if request.method == "DELETE":
        conn.execute("DELETE FROM medicos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Médico eliminado"})

    if request.method == "PUT":
        data = request.json
        conn.execute(
            "UPDATE medicos SET nombre = ?, especialidad_id = ?, telefono = ?, email = ? WHERE id = ?",
            (
                data["nombre"],
                data["especialidad_id"],
                data.get("telefono"),
                data.get("email"),
                id,
            ),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Médico actualizado"})


# --- PACIENTES ---
@app.route("/api/pacientes", methods=["GET", "POST"])
def manage_pacientes():
    conn = get_db_connection()

    if request.method == "POST":
        data = request.json
        try:
            conn.execute(
                "INSERT INTO pacientes (nombre, documento, telefono, email, fecha_nacimiento) VALUES (?, ?, ?, ?, ?)",
                (
                    data["nombre"],
                    data["documento"],
                    data.get("telefono"),
                    data.get("email"),
                    data.get("fecha_nacimiento"),
                ),
            )
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return (
                jsonify(
                    {"error": "El número de documento ya está registrado"}
                ),
                400,
            )
        conn.close()
        return jsonify({"message": "Paciente registrado exitosamente"}), 201

    items = conn.execute("SELECT * FROM pacientes").fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])


@app.route("/api/pacientes/<int:id>", methods=["PUT", "DELETE"])
def update_delete_paciente(id):
    conn = get_db_connection()

    if request.method == "DELETE":
        conn.execute("DELETE FROM pacientes WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Paciente eliminado"})

    if request.method == "PUT":
        data = request.json
        conn.execute(
            "UPDATE pacientes SET nombre = ?, documento = ?, telefono = ?, email = ?, fecha_nacimiento = ? WHERE id = ?",
            (
                data["nombre"],
                data["documento"],
                data.get("telefono"),
                data.get("email"),
                data.get("fecha_nacimiento"),
                id,
            ),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Paciente actualizado"})


# --- CITAS ---
@app.route("/api/citas", methods=["GET", "POST"])
def manage_citas():
    conn = get_db_connection()

    if request.method == "POST":
        data = request.json
        conn.execute(
            "INSERT INTO citas (paciente_id, medico_id, fecha, hora, motivo, estado) VALUES (?, ?, ?, ?, ?, ?)",
            (
                data["paciente_id"],
                data["medico_id"],
                data["fecha"],
                data["hora"],
                data.get("motivo", ""),
                data.get("estado", "Programada"),
            ),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Cita agendada exitosamente"}), 201

    query = """
        SELECT c.id, c.fecha, c.hora, c.motivo, c.estado,
               p.id as paciente_id, p.nombre as paciente_nombre, p.documento as paciente_doc,
               m.id as medico_id, m.nombre as medico_nombre, e.nombre as especialidad
        FROM citas c
        JOIN pacientes p ON c.paciente_id = p.id
        JOIN medicos m ON c.medico_id = m.id
        JOIN especialidades e ON m.especialidad_id = e.id
        ORDER BY c.fecha ASC, c.hora ASC
    """
    items = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])


@app.route("/api/citas/<int:id>", methods=["PUT", "DELETE"])
def update_delete_cita(id):
    conn = get_db_connection()

    if request.method == "DELETE":
        conn.execute("DELETE FROM citas WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Cita cancelada/eliminada"})

    if request.method == "PUT":
        data = request.json
        conn.execute(
            "UPDATE citas SET paciente_id = ?, medico_id = ?, fecha = ?, hora = ?, motivo = ?, estado = ? WHERE id = ?",
            (
                data["paciente_id"],
                data["medico_id"],
                data["fecha"],
                data["hora"],
                data.get("motivo", ""),
                data.get("estado", "Programada"),
                id,
            ),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Cita actualizada"})


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)