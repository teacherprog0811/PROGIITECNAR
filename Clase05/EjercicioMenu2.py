def Menu():
    print('''####### MENU PRINCIPAL ####### \n 
            1. Personas 
            2. Vehiculos 
            3. Universidades 
            4. Notas 
            5. Salir \n
####### UNITECNAR #######''')
    
opcion =1
while opcion <= 5:
    Menu()
    opcion = int(input("Elige una opcion del menu: "))
    if opcion == 1:
            print ("Haz elegido la opcion del menu Personas")
           
    if opcion == 2:
            print ("Haz elegido la opcion del menu Vehiculos")
          
    if opcion == 3:
            print ("Haz elegido la opcion del menu Universidades")
           
    if opcion == 4:
            print ("Haz elegido la opcion del menu Notas")
            
    if opcion == 5:
            print ("Gracias por utilizar nuestra App. \n")
            break
    else:
           print ("HAS SELECCIONADO UNA OPCION INCORRECTA INTENTALO DE NUEVO  (1 - 5) \n")
           opcion = 0