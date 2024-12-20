import facultades
import carreras
import cursos
import estudiantes
import asignaciones
import busqueda

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Menú de Facultades")
    print("2. Menú de Carreras")
    print("3. Menú de Cursos")
    print("4. Menú de Estudiantes")
    print("5. Menú de Asignaciones")
    print("6. Menú de Búsqueda")
    print("7. Salir")

def main():
    while True:  # Bucle principal
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            facultades.menu_facultades()  # Entrar al menú de facultades
        elif opcion == "2":
            carreras.menu_carreras()
        elif opcion == "3":
            cursos.menu_cursos()
        elif opcion == "4":
            estudiantes.menu_estudiantes()
        elif opcion == "5":
            asignaciones.menu_asignaciones()
        elif opcion == "6":
            busqueda.menu_busqueda()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
