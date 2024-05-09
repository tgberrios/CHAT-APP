import sqlite3

def conectar_db():
    conexion = sqlite3.connect('data.db')
    return conexion

def registrar_usuario():
    conexion = conectar_db()
    cursor = conexion.cursor()

    usuario = input("Elige tu usuario: ")
    password = input("Elige tu password: ")

    cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
    conexion.commit()
    conexion.close()

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
        return True
    else:
        print("Usuario o Password incorrectos!")
        return False
    
    return resultado

def user_logged(resultado):
    choice = ""
    if resultado == True:
        print("1. Ver Chats")
        print("2. Nuevo Chat")
        print("3. Eliminar Chat")
    else:
        print("Error Critico contactar -> tgberrios@outlook.com")

        if choice == "1":
            verChats()
        elif choice == "2":
            nuevoChat()
        elif choice == "3":
            eliminarchat()
        else:
            "Opcion no valida!"  


def main():
    while True:
        print("CR TEAM")
        print("1.Registrar Usuario")
        print("2.Iniciar Sesión")
        print("3.Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            registrar_usuario()
        elif choice == "2":
            iniciar_sesion()
        elif choice == "3":
            break
        else:
            print("Opción no válida!")

if __name__ == "__main__":
    main()
