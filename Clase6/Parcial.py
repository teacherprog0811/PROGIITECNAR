def menu_principal():
    while True:
        print("MENU PRINCIPAL")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            submenu_opcion_1()
        elif opcion == "2":
            submenu_opcion_2()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


def submenu_opcion_1():
    while True:
        print("\nSUBMENU - Opción 1")
        print("1. Subopción 1")
        print("2. Subopción 2")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ha seleccionado la subopción 1.")
        elif opcion == "2":
            print("Ha seleccionado la subopción 2.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


def submenu_opcion_2():
    while True:
        print("\nSUBMENU - Opción 2")
        print("1. Subopción A")
        print("2. Subopción B")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Ha seleccionado la subopción A.")
        elif opcion == "2":
            print("Ha seleccionado la subopción B.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")


# Ejecutar el menú principal
menu_principal()
