class Personas:

    def menu(self):
        while True:
            print("\nMENU PERSONAS")
            print("1. Crear")
            print("2. Listar")
            print("3. Eliminar")
            print("4. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(Personas.agregar())
            elif opcion == "2":
                print(Personas.listar())
            elif opcion == "3":
                print(Personas.eliminar())
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.")
    
    def agregar():
        return f'HAZ SELECCIONADO LA FUNCIONALIDAD AGREGAR'
    
    def listar():   
        return f'HAZ SELECCIONADO LA FUNCIONALIDAD LISTAR'
    
    def eliminar(): 
        return f'HAZ SELECCIONADO LA FUNCIONALIDAD ELIMINAR'
