import json
import os

FACULTADES_FILE = "data/facultades.json"

def cargar_facultades():
    if not os.path.exists(FACULTADES_FILE):
        # Si el archivo no existe, crearlo con una lista vacía
        with open(FACULTADES_FILE, "w") as file:
            json.dump([], file)
        return []

    # Manejar archivo vacío o con formato incorrecto
    try:
        with open(FACULTADES_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Si el archivo está vacío o da error, retornar una lista vacía
        print(f"Advertencia: El archivo '{FACULTADES_FILE}' está vacío o corrupto. Se inicializará nuevamente.")
        return []


def guardar_facultades(data):
    with open(FACULTADES_FILE, "w") as file:
        json.dump(data, file, indent=4)

def menu_facultades():
    while True:
        print("\n--- MENÚ DE FACULTADES ---")
        print("1. Crear Facultad")
        print("2. Mostrar Facultades")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_facultad()
        elif opcion == "2":
            mostrar_facultades()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def crear_facultad():
    codigo = input("Ingrese el código de la facultad: ")
    nombre = input("Ingrese el nombre de la facultad: ")

    facultades = cargar_facultades()
    for facultad in facultades:
        if facultad['codigo'] == codigo:
            print("Error: El código de facultad ya existe.")
            return

    facultades.append({"codigo": codigo, "nombre": nombre})
    guardar_facultades(facultades)
    print("Facultad creada exitosamente.")

def mostrar_facultades():
    facultades = cargar_facultades()
    if not facultades:
        print("No hay facultades registradas.")
        return
    print("\n--- LISTA DE FACULTADES ---")
    for f in facultades:
        print(f"Código: {f['codigo']}, Nombre: {f['nombre']}")
