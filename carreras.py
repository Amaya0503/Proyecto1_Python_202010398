import json
import os
import facultades  # Para validar facultades

CARRERAS_FILE = "data/carreras.json"

def cargar_carreras():
    if not os.path.exists(CARRERAS_FILE):
        with open(CARRERAS_FILE, "w") as file:
            json.dump([], file)
        return []

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
    facultad_codigo = input("Ingrese el código de la facultad: ")
    facultades_list = facultades.cargar_facultades()

    # Validar que la facultad exista
    facultad = next((f for f in facultades_list if f["codigo"] == facultad_codigo), None)
    if not facultad:
        print("Error: La facultad no existe. No se puede crear la carrera.")
        return

    codigo = input("Ingrese el código de la carrera: ")
    nombre = input("Ingrese el nombre de la carrera: ")

    carreras = cargar_carreras()
    if any(c["codigo"] == codigo for c in carreras):
        print("Error: El código de la carrera ya existe.")
        return

    carreras.append({"codigo": codigo, "nombre": nombre, "facultad": facultad_codigo})
    guardar_carreras(carreras)
    print(f"Carrera '{nombre}' creada exitosamente en la facultad '{facultad['nombre']}'.")

def mostrar_carreras():
    carreras = cargar_carreras()
    if not carreras:
        print("No hay carreras registradas.")
        return
    print("\n--- LISTA DE CARRERAS ---")
    for c in carreras:
        print(f"Código: {c['codigo']}, Nombre: {c['nombre']}, Facultad: {c['facultad']}")
