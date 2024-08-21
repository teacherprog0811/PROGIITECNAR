from tkinter import * 

def mostrardatos():
    lnombreFrame=Label(marco, text=cnombre.get())
    lnombreFrame.pack()
    lapellidoFrame=Label(marco, text=capellido.get())
    lapellidoFrame.pack()
    ledadFrame=Label(marco, text=cedad.get())
    ledadFrame.pack()
    ldirFrame=Label(marco, text=cdireccion.get())
    ldirFrame.pack()
    ltelFrame=Label(marco, text=ctelefono.get())
    ltelFrame.pack()
    LframeSexo = Label(marco, text=sexofinal)
    LframeSexo.pack()
    #Pintar la ciudad
    seleccionados = cciudad.curselection()
    for index in seleccionados:
        elemento = cciudad.get(index)
        LframeCiudad = Label(marco, text=elemento)
        LframeCiudad.pack()

def obtener_seleccion():
    seleccion = variablesexo.get()
    global sexofinal
    if seleccion == 1:
         sexofinal = "Hombre"
    elif seleccion == 2:
        sexofinal = "Mujer"

ventana = Tk()
variablesexo = IntVar()
# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Creacion de labels
inicio = Label(ventana, text = "Formulario de registro", font="Arial",padx=50)
lnombre = Label(ventana, text = "Nombre:",padx=0)
lapellido = Label(ventana, text = "Apellido:",padx=0)
ledad = Label(ventana, text = "Edad:",padx=0)
ldireccion = Label(ventana, text = "Direccion:",padx=0)
ltelefono = Label(ventana, text = "Telefono:",padx=0)

#Definiendo posiciones 
inicio.place(x=10, y=30)
lnombre.place(x=10, y=70)
lapellido.place(x=10, y=100)
ledad.place(x=10, y=130)
ldireccion.place(x=10, y=160)
ltelefono.place(x=10, y=190)

# Creando cajas de texto con Entry
cnombre = Entry(ventana, width=50)
capellido = Entry(ventana, width=50)
cedad = Entry(ventana, width=50)
cdireccion = Entry(ventana, width=50)
ctelefono = Entry(ventana, width=50)

# Definiendo posisicones para cajas de texto
cnombre.place(x=70, y=70)
capellido.place(x=70, y=100)
cedad.place(x=70, y=130)
cdireccion.place(x=70, y=160)
ctelefono.place(x=70, y=190)

lsexo = Label(ventana, text="Sexo")
lsexo.place(x=70,y=220)
rsexom = Radiobutton(ventana, text="Masculino", variable=variablesexo, value=1, command=obtener_seleccion)
rsexom.place(x=70,y=250)
rsexof = Radiobutton(ventana, text="Femenino", variable=variablesexo, value=2, command=obtener_seleccion)
rsexof.place(x=70,y=280)

lciudad = Label(ventana, text="Ciudad")

lciudad.place(x=70,y=310)

elementos = ["Cartagena", "Barranquilla", "Bogota", "Cali"]

vciudad = Variable(value=elementos)

#for elemento in elementos:
#    cciudad.insert(tk.END, elemento)

cciudad = Listbox(ventana, selectmode="Single", listvariable=vciudad)
cciudad.place(x=70,y=330)

#Creando boton
boton = Button(ventana, text = "Registrar", padx=10, pady=5,command=mostrardatos)
boton.place(x=100, y=500)

marco = Frame(ventana,width=400, height=180, padx=100,bd=1, relief="raised")
marco.place(x=70, y=600)



mainloop()
