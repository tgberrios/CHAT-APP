import sqlite3

# Función para conectar a la base de datos SQLite
def conectar_db():
    conexion = sqlite3.connect('data.db')
    cursor = conexion.cursor()

    # Crear la tabla 'chats' si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS chats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        remitente TEXT,
                        destinatario TEXT,
                        mensaje TEXT,
                        fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')

    # Crear la tabla 'usuarios' si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT UNIQUE,
                        password TEXT
                    )''')

    conexion.commit()

    return conexion

# Función para registrar un nuevo usuario en la base de datos
def registrar_usuario():
    conexion = conectar_db()
    cursor = conexion.cursor()

    usuario = input("Elige tu usuario: ")
    password = input("Elige tu password: ")

    cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
    conexion.commit()
    conexion.close()

# Función para iniciar sesión y devolver el usuario autenticado
def iniciar_sesion():
    usuario = input("Usuario: ")
    password = input("Password: ")

    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND password = ?", (usuario, password))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        print("Te has autenticado con éxito!")
        return resultado  # Devuelve el usuario autenticado
    else:
        print("Usuario o Password incorrectos!")
        return None

# Función para ver los chats del usuario
def verChats(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consulta SQL para obtener los chats del usuario autenticado
    cursor.execute("SELECT remitente, destinatario, mensaje, fecha_hora FROM chats WHERE remitente = ? OR destinatario = ? ORDER BY fecha_hora", (usuario_id, usuario_id))
    chats = cursor.fetchall()

    print("DEBUG: Chats recuperados:", chats)  # Mensaje de depuración

    # Mostrar los chats
    if chats:
        print("Mostrando Chats:")
        for chat in chats:
            remitente, destinatario, mensaje, fecha_hora = chat
            print(f"De: {remitente} | Para: {destinatario} | Mensaje: {mensaje} | Fecha/Hora: {fecha_hora}")
    else:
        print("No hay chats disponibles.")

    conexion.close()

# Función para enviar un mensaje a otro usuario
def enviarMensaje(remitente, mensaje):
    destinatario = input("Ingresa el nombre de usuario del destinatario: ")

    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO chats (remitente, destinatario, mensaje) VALUES (?, ?, ?)", (remitente, destinatario, mensaje))
    conexion.commit()
    conexion.close()

    print("Mensaje enviado con éxito!")

# Función para mostrar el menú después de iniciar sesión
def menu(usuario):
    print(f"Bienvenido, {usuario[1]}!")

    while True:
        print("1. Ver Chats")
        print("2. Enviar Mensaje")
        print("3. Salir")
        choice = input("Ingresa qué quieres hacer: ")

        if choice == "1":
            verChats(usuario[0])  # Pasa el ID del usuario autenticado a la función verChats()
        elif choice == "2":
            destinatario = input("Ingresa el nombre de usuario del destinatario: ")
            mensaje = input("Escribe tu mensaje: ")
            enviarMensaje(usuario[1], mensaje)  # Pasa el remitente, destinatario y mensaje
        elif choice == "3":
            break
        else:
            print("Opción no válida!")

# Función principal que ejecuta el programa
def main():
    while True:
        print("CR TEAM")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            registrar_usuario()
        elif choice == "2":
            usuario_autenticado = iniciar_sesion()
            if usuario_autenticado:
                menu(usuario_autenticado)  # Llama al menú pasando el usuario autenticado
        elif choice == "3":
            break
        else:
            print("Opción no válida!")

if __name__ == "__main__":
    main()
