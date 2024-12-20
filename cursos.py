import json
import os

CURSOS_FILE = "data/cursos.json"

def cargar_cursos():
    if not os.path.exists(CURSOS_FILE):
        # Si el archivo no existe, crearlo con una lista vacía
        with open(CURSOS_FILE, "w") as file:
            json.dump([], file)
        return []

    # Manejar archivo vacío o con formato incorrecto
    try:
        with open(CURSOS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Advertencia: El archivo '{CURSOS_FILE}' está vacío o corrupto. Se inicializará nuevamente.")
        return []


def guardar_cursos(data):
    with open(CURSOS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def menu_cursos():
    while True:
        print("\n--- MENÚ DE CURSOS ---")
        print("1. Crear Curso")
        print("2. Mostrar Cursos")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_curso()
        elif opcion == "2":
            mostrar_cursos()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def crear_curso():
    carrera = input("Ingrese el código de la carrera: ")
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")

    cursos = cargar_cursos()
    for curso in cursos:
        if curso['codigo'] == codigo:
            print("Error: El código del curso ya existe.")
            return

    cursos.append({"codigo": codigo, "nombre": nombre, "carrera": carrera})
    guardar_cursos(cursos)
    print("Curso creado exitosamente.")

def mostrar_cursos():
    cursos = cargar_cursos()
    if not cursos:
        print("No hay cursos registrados.")
        return
    print("\n--- LISTA DE CURSOS ---")
    for curso in cursos:
        print(f"Código: {curso['codigo']}, Nombre: {curso['nombre']}, Carrera: {curso['carrera']}")
