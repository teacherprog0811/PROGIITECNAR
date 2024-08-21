def Menu():
    print("Elige una opcion del menu \n 1. Personas \n 2. Vehiculos \n 3. Universidades \n 4. Notas \n 5. Salir \n")
    

Menu()
opcion = int(input("Elige una opcion del menu: \n"))
if opcion == 1:
    print ("Haz elegido la opcion del menu Personas")
    Menu()
elif opcion == 2:
    print ("Haz elegido la opcion del menu Vehiculos")
    Menu()
elif opcion == 3:
    print ("Haz elegido la opcion del menu Universidades")
    Menu()
elif opcion == 4:
    print ("Haz elegido la opcion del menu Notas")
    Menu()
elif opcion == 5:
    print ("Gracias por utilizar nuestra App. \n")
    SystemExit
else:
        print ("Elige una opcion del menu entre 1 - 5 \n")
        Menu()