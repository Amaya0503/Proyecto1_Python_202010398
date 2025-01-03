import json
import os
import facultades
import carreras

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

    # Solicitar la facultad y carrera del estudiante
    facultad_codigo = input("Ingrese el código de la facultad del estudiante: ")
    carrera_codigo = input("Ingrese el código de la carrera del estudiante: ")

    # Validar que la facultad y carrera existan
    facultades_list = facultades.cargar_facultades()
    carreras_list = carreras.cargar_carreras()

    facultad = next((f for f in facultades_list if f["codigo"] == facultad_codigo), None)
    if not facultad:
        print("Error: La facultad no existe.")
        return

    carrera = next((c for c in carreras_list if c["codigo"] == carrera_codigo), None)
    if not carrera or carrera["facultad"] != facultad_codigo:
        print("Error: La carrera no existe o no pertenece a la facultad indicada.")
        return

    estudiantes_list = cargar_estudiantes()
    if any(e["carnet"] == carnet for e in estudiantes_list):
        print("Error: El carnet ya existe.")
        return

    estudiantes_list.append({
        "carnet": carnet,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "estado": "activo",
        "cursos": [],
        "facultad": facultad_codigo,
        "carrera": carrera_codigo
    })
    guardar_estudiantes(estudiantes_list)
    print("Estudiante creado exitosamente.")

def mostrar_estudiantes():
    estudiantes_list = cargar_estudiantes()
    if not estudiantes_list:
        print("No hay estudiantes registrados.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for e in estudiantes_list:
        print(f"Carnet: {e['carnet']}, Nombre: {e['nombre']} {e['apellido']}, Edad: {e['edad']}, Estado: {e['estado']}")
        print(f"Facultad: {e['facultad']}, Carrera: {e['carrera']}")
        print(f"Cursos Asignados: {', '.join(e['cursos']) if e['cursos'] else 'Ninguno'}")
