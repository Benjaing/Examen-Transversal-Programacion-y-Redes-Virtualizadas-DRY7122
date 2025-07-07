from flask import Flask, request, redirect, render_template_string
import sqlite3
import bcrypt

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nombre TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password'].encode('utf-8')

        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()
        c.execute("SELECT password_hash FROM usuarios WHERE nombre = ?", (nombre,))
        row = c.fetchone()
        conn.close()

        if row and bcrypt.checkpw(password, row[0].encode('utf-8')):
            mensaje = 'Usuario validado correctamente.'
        else:
            mensaje = 'Usuario o contraseña incorrectos.'

    return render_template_string('''
        <h2>Ingreso de Usuarios</h2>
        <form method="POST">
            Nombre: <input name="nombre"><br>
            Contraseña: <input name="password" type="password"><br>
            <button type="submit">Validar</button>
        </form>
        <p>{{mensaje}}</p>
    ''', mensaje=mensaje)

def agregar_usuario(nombre, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"El usuario '{nombre}' ya existe.")
    conn.close()

if __name__ == '__main__':
    init_db()

    integrantes = {
        'Benjamin': 'cisco123',
        'Renato': 'cisco321',
    }

    for nombre, clave in integrantes.items():
        agregar_usuario(nombre, clave)

    app.run(port=5800)
