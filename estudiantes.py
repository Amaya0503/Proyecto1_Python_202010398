import json
import os

ESTUDIANTES_FILE = "data/estudiantes.json"

def cargar_estudiantes():
    if not os.path.exists(ESTUDIANTES_FILE):
        with open(ESTUDIANTES_FILE, "w") as file:
            json.dump([], file)
        return []

    try:
        with open(ESTUDIANTES_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Advertencia: El archivo '{ESTUDIANTES_FILE}' está vacío o corrupto.")
        return []

def guardar_estudiantes(data):
    with open(ESTUDIANTES_FILE, "w") as file:
        json.dump(data, file, indent=4)

def menu_estudiantes():
    while True:
        print("\n--- MENÚ DE ESTUDIANTES ---")
        print("1. Crear Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def crear_estudiante():
    carnet = input("Ingrese el carnet del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")

    estudiantes = cargar_estudiantes()
    if any(e["carnet"] == carnet for e in estudiantes):
        print("Error: El carnet ya existe.")
        return

    estudiantes.append({"carnet": carnet, "nombre": nombre, "apellido": apellido, "edad": edad, "estado": "activo", "cursos": []})
    guardar_estudiantes(estudiantes)
    print("Estudiante creado exitosamente.")

def mostrar_estudiantes():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for e in estudiantes:
        print(f"Carnet: {e['carnet']}, Nombre: {e['nombre']} {e['apellido']}, Edad: {e['edad']}, Estado: {e['estado']}")
