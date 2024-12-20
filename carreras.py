import json
import os

CARRERAS_FILE = "data/carreras.json"

def cargar_carreras():
    if not os.path.exists(CARRERAS_FILE):
        # Si el archivo no existe, crearlo con una lista vacía
        with open(CARRERAS_FILE, "w") as file:
            json.dump([], file)
        return []

    # Manejar archivo vacío o con formato incorrecto
    try:
        with open(CARRERAS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Advertencia: El archivo '{CARRERAS_FILE}' está vacío o corrupto. Se inicializará nuevamente.")
        return []


def guardar_carreras(data):
    with open(CARRERAS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def menu_carreras():
    while True:
        print("\n--- MENÚ DE CARRERAS ---")
        print("1. Crear Carrera")
        print("2. Mostrar Carreras")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_carrera()
        elif opcion == "2":
            mostrar_carreras()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def crear_carrera():
    facultad = input("Ingrese el código de la facultad: ")
    codigo = input("Ingrese el código de la carrera: ")
    nombre = input("Ingrese el nombre de la carrera: ")

    carreras = cargar_carreras()
    for c in carreras:
        if c['codigo'] == codigo:
            print("Error: El código de la carrera ya existe.")
            return

    carreras.append({"codigo": codigo, "nombre": nombre, "facultad": facultad})
    guardar_carreras(carreras)
    print("Carrera creada exitosamente.")

def mostrar_carreras():
    carreras = cargar_carreras()
    if not carreras:
        print("No hay carreras registradas.")
        return
    print("\n--- LISTA DE CARRERAS ---")
    for c in carreras:
        print(f"Código: {c['codigo']}, Nombre: {c['nombre']}, Facultad: {c['facultad']}")
