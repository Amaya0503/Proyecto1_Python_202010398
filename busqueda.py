import estudiantes
import cursos
import carreras
import facultades

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
    estudiantes_list = estudiantes.cargar_estudiantes()

    estudiante = next((e for e in estudiantes_list if e["carnet"] == carnet), None)
    if estudiante:
        print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")
        print(f"Nombre: {estudiante['nombre']} {estudiante['apellido']}")
        print(f"Edad: {estudiante['edad']}, Estado: {estudiante['estado']}")
        print(f"Cursos Asignados: {', '.join(estudiante['cursos']) if estudiante['cursos'] else 'Ninguno'}")
    else:
        print("Error: Estudiante no encontrado.")

def buscar_curso():
    codigo = input("Ingrese el código del curso: ")
    cursos_list = cursos.cargar_cursos()

    curso = next((c for c in cursos_list if c["codigo"] == codigo), None)
    if curso:
        print("\n--- INFORMACIÓN DEL CURSO ---")
        print(f"Código: {curso['codigo']}, Nombre: {curso['nombre']}")
        print(f"Carrera: {curso['carrera']}")
    else:
        print("Error: Curso no encontrado.")

def buscar_carrera():
    codigo = input("Ingrese el código de la carrera: ")
    carreras_list = carreras.cargar_carreras()

    carrera = next((c for c in carreras_list if c["codigo"] == codigo), None)
    if carrera:
        print("\n--- INFORMACIÓN DE LA CARRERA ---")
        print(f"Código: {carrera['codigo']}, Nombre: {carrera['nombre']}")
        print(f"Facultad: {carrera['facultad']}")
    else:
        print("Error: Carrera no encontrada.")

def buscar_facultad():
    codigo = input("Ingrese el código de la facultad: ")
    facultades_list = facultades.cargar_facultades()

    facultad = next((f for f in facultades_list if f["codigo"] == codigo), None)
    if facultad:
        print("\n--- INFORMACIÓN DE LA FACULTAD ---")
        print(f"Código: {facultad['codigo']}, Nombre: {facultad['nombre']}")
    else:
        print("Error: Facultad no encontrada.")
