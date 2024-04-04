from Personas import Personas

def menu_principal():
    while True:
        print("MENU PRINCIPAL")
        print("1. Personas")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            p = Personas()
            print(p.menu())
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


# Ejecutar el menú principal
menu_principal()