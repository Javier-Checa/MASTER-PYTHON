from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria para almacenar las tareas
tareas = ["Aprender Flask", "Crear interfaz HTML"]

@app.route("/")
def inicio():
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    nueva_tarea = request.form.get("tarea")
    if nueva_tarea and nueva_tarea.strip():
        tareas.append(nueva_tarea.strip())
    return redirect(url_for("inicio"))