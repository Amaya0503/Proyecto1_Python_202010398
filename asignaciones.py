import estudiantes
import cursos
import carreras
import facultades

def cargar_estudiantes():
    return estudiantes.cargar_estudiantes()

def cargar_cursos():
    return cursos.cargar_cursos()

def cargar_carreras():
    return carreras.cargar_carreras()

def cargar_facultades():
    return facultades.cargar_facultades()

def guardar_estudiantes(data):
    estudiantes.guardar_estudiantes(data)

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

    estudiantes_list = cargar_estudiantes()
    cursos_list = cargar_cursos()
    carreras_list = cargar_carreras()
    facultades_list = cargar_facultades()

    # Validar que el estudiante exista
    estudiante = next((e for e in estudiantes_list if e["carnet"] == carnet), None)
    if not estudiante:
        print("Error: El estudiante no existe.")
        return

    # Validar que el estudiante esté activo
    if estudiante["estado"] != "activo":
        print("Error: El estudiante no está activo.")
        return

    # Validar que el curso exista
    curso = next((c for c in cursos_list if c["codigo"] == codigo_curso), None)
    if not curso:
        print("Error: El curso no existe.")
        return

    # Obtener la carrera del curso
    carrera = next((c for c in carreras_list if c["codigo"] == curso["carrera"]), None)
    if not carrera:
        print("Error: La carrera asociada al curso no existe.")
        return

    # Obtener la facultad de la carrera
    facultad = next((f for f in facultades_list if f["codigo"] == carrera["facultad"]), None)
    if not facultad:
        print("Error: La facultad asociada a la carrera no existe.")
        return

    # Validar que el estudiante pertenezca a la facultad y carrera
    if estudiante.get("facultad") != facultad["codigo"] or estudiante.get("carrera") != carrera["codigo"]:
        print(f"Error: El estudiante no pertenece a la facultad '{facultad['nombre']}' ni a la carrera '{carrera['nombre']}'.")
        return

    # Validar que el curso no esté ya asignado
    if codigo_curso in estudiante["cursos"]:
        print("Error: El curso ya está asignado a este estudiante.")
        return

    # Asignar el curso
    estudiante["cursos"].append(codigo_curso)
    guardar_estudiantes(estudiantes_list)
    print(f"Curso '{codigo_curso}' asignado exitosamente al estudiante '{carnet}'.")

def mostrar_asignaciones():
    estudiantes_list = cargar_estudiantes()
    if not estudiantes_list:
        print("No hay asignaciones registradas.")
        return

    print("\n--- ASIGNACIONES DE CURSOS ---")
    for e in estudiantes_list:
        print(f"Estudiante: {e['nombre']} {e['apellido']} (Carnet: {e['carnet']})")
        if e["cursos"]:
            print("  Cursos asignados:")
            for curso in e["cursos"]:
                print(f"    - {curso}")
        else:
            print("  No tiene cursos asignados.")
