import json
import os

ESTUDIANTES_FILE = "data/estudiantes.json"
CURSOS_FILE = "data/cursos.json"

def cargar_estudiantes():
    if not os.path.exists(ESTUDIANTES_FILE):
        return []
    with open(ESTUDIANTES_FILE, "r") as file:
        return json.load(file)

def guardar_estudiantes(data):
    with open(ESTUDIANTES_FILE, "w") as file:
        json.dump(data, file, indent=4)

def cargar_cursos():
    if not os.path.exists(CURSOS_FILE):
        return []
    with open(CURSOS_FILE, "r") as file:
        return json.load(file)

def menu_asignaciones():
    while True:
        print("\n--- MENÚ DE ASIGNACIONES ---")
        print("1. Asignar Curso a Estudiante")
        print("2. Mostrar Asignaciones")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            asignar_curso()
        elif opcion == "2":
            mostrar_asignaciones()
        elif opcion == "3":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def asignar_curso():
    carnet = input("Ingrese el carnet del estudiante: ")
    codigo_curso = input("Ingrese el código del curso: ")

    estudiantes = cargar_estudiantes()
    cursos = cargar_cursos()

    estudiante = next((e for e in estudiantes if e["carnet"] == carnet), None)
    curso = next((c for c in cursos if c["codigo"] == codigo_curso), None)

    if not estudiante:
        print("Error: El estudiante no existe.")
        return
    if estudiante["estado"] != "activo":
        print("Error: El estudiante no está activo.")
        return
    if not curso:
        print("Error: El curso no existe.")
        return

    # Verificar si ya está asignado
    if codigo_curso in estudiante["cursos"]:
        print("Error: El curso ya está asignado a este estudiante.")
        return

    # Asignar curso
    estudiante["cursos"].append(codigo_curso)
    guardar_estudiantes(estudiantes)
    print(f"Curso '{codigo_curso}' asignado exitosamente al estudiante '{carnet}'.")

def mostrar_asignaciones():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay asignaciones registradas.")
        return

    print("\n--- ASIGNACIONES DE CURSOS ---")
    for e in estudiantes:
        print(f"Estudiante: {e['nombre']} {e['apellido']} (Carnet: {e['carnet']})")
        if e["cursos"]:
            print("  Cursos asignados:")
            for curso in e["cursos"]:
                print(f"    - {curso}")
        else:
            print("  No tiene cursos asignados.")
