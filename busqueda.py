import json
import os

ESTUDIANTES_FILE = "data/estudiantes.json"
CURSOS_FILE = "data/cursos.json"
CARRERAS_FILE = "data/carreras.json"
FACULTADES_FILE = "data/facultades.json"

def cargar_datos(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return json.load(file)

def menu_busqueda():
    while True:
        print("\n--- MENÚ DE BÚSQUEDA ---")
        print("1. Buscar Estudiante por Carnet")
        print("2. Buscar Curso por Código")
        print("3. Buscar Carrera por Código")
        print("4. Buscar Facultad por Código")
        print("5. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar_estudiante_por_carnet()
        elif opcion == "2":
            buscar_curso()
        elif opcion == "3":
            buscar_carrera()
        elif opcion == "4":
            buscar_facultad()
        elif opcion == "5":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def buscar_estudiante_por_carnet():
    carnet = input("Ingrese el carnet del estudiante: ")
    estudiantes = cargar_datos(ESTUDIANTES_FILE)

    estudiante = next((e for e in estudiantes if e["carnet"] == carnet), None)
    if estudiante:
        print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Edad: {estudiante['edad']}, Estado: {estudiante['estado']}")
        print(f"Cursos Asignados: {', '.join(estudiante['cursos']) if estudiante['cursos'] else 'Ninguno'}")
    else:
        print("Error: Estudiante no encontrado.")

def buscar_curso():
    codigo = input("Ingrese el código del curso: ")
    cursos = cargar_datos(CURSOS_FILE)

    curso = next((c for c in cursos if c["codigo"] == codigo), None)
    if curso:
        print("\n--- INFORMACIÓN DEL CURSO ---")
        print(f"Código: {curso['codigo']}, Nombre: {curso['nombre']}")
        print(f"Carrera: {curso['carrera']}")
    else:
        print("Error: Curso no encontrado.")

def buscar_carrera():
    codigo = input("Ingrese el código de la carrera: ")
    carreras = cargar_datos(CARRERAS_FILE)

    carrera = next((c for c in carreras if c["codigo"] == codigo), None)
    if carrera:
        print("\n--- INFORMACIÓN DE LA CARRERA ---")
        print(f"Código: {carrera['codigo']}, Nombre: {carrera['nombre']}")
        print(f"Facultad: {carrera['facultad']}")
    else:
        print("Error: Carrera no encontrada.")

def buscar_facultad():
    codigo = input("Ingrese el código de la facultad: ")
    facultades = cargar_datos(FACULTADES_FILE)

    facultad = next((f for f in facultades if f["codigo"] == codigo), None)
    if facultad:
        print("\n--- INFORMACIÓN DE LA FACULTAD ---")
        print(f"Código: {facultad['codigo']}, Nombre: {facultad['nombre']}")
    else:
        print("Error: Facultad no encontrada.")
