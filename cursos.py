import json
import os
import carreras  # Para validar carreras

CURSOS_FILE = "data/cursos.json"

def cargar_cursos():
    if not os.path.exists(CURSOS_FILE):
        with open(CURSOS_FILE, "w") as file:
            json.dump([], file)
        return []

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
    carrera_codigo = input("Ingrese el código de la carrera: ")
    carreras_list = carreras.cargar_carreras()

    # Validar que la carrera exista
    carrera = next((c for c in carreras_list if c["codigo"] == carrera_codigo), None)
    if not carrera:
        print("Error: La carrera no existe. No se puede crear el curso.")
        return

    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")

    cursos = cargar_cursos()
    if any(c["codigo"] == codigo for c in cursos):
        print("Error: El código del curso ya existe.")
        return

    cursos.append({"codigo": codigo, "nombre": nombre, "carrera": carrera_codigo})
    guardar_cursos(cursos)
    print(f"Curso '{nombre}' creado exitosamente en la carrera '{carrera['nombre']}'.")

def mostrar_cursos():
    cursos = cargar_cursos()
    if not cursos:
        print("No hay cursos registrados.")
        return
    print("\n--- LISTA DE CURSOS ---")
    for curso in cursos:
        print(f"Código: {curso['codigo']}, Nombre: {curso['nombre']}, Carrera: {curso['carrera']}")
