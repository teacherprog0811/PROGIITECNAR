import tkinter as tk

def mostrardatos():
    lnombreFrame=tk.Label(marco, text=cnombre.get())
    lnombreFrame.pack()
    lapellidoFrame=tk.Label(marco, text=capellido.get())
    lapellidoFrame.pack()
    ledadFrame=tk.Label(marco, text=cedad.get())
    ledadFrame.pack()
    ldirFrame=tk.Label(marco, text=cdireccion.get())
    ldirFrame.pack()
    ltelFrame=tk.Label(marco, text=ctelefono.get())
    ltelFrame.pack()

ventana = tk.Tk()
# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Creacion de labels
inicio = tk.Label(ventana, text = "Formulario de registro", font="Arial")
lnombre = tk.Label(ventana, text = "Nombre:")
lapellido = tk.Label(ventana, text = "Apellido:")
ledad = tk.Label(ventana, text = "Edad:")
ldireccion = tk.Labelabel(ventana, text = "Direccion:")
ltelefono = tk.Label(ventana, text = "Telefono:")

#Definiendo posiciones 
inicio.grid(row = 0, column = 0, columnspan=2)
lnombre.grid(row = 1, column = 0,pady=2)
lapellido.grid(row = 2, column = 0)
ledad.grid(row = 3, column = 0)
ldireccion.grid(row = 4, column = 0)
ltelefono.grid(row = 5, column = 0)

# Creando cajas de texto con Entry
cnombre = tk.Entry(ventana, width=50)
capellido = tk.Entry(ventana, width=50)
cedad = tk.Entry(ventana, width=50)
cdireccion = tk.Entry(ventana, width=50)
ctelefono = tk.Entry(ventana, width=50)

# Definiendo posisicones para cajas de texto
cnombre.grid(row = 1, column = 1,pady=4)
capellido.grid(row = 2, column = 1)
cedad.grid(row = 3, column = 1)
cdireccion.grid(row = 4, column = 1)
ctelefono.grid(row = 5, column = 1)

#Creando boton

boton = tk.Button(ventana, text = "Registrar", command=mostrardatos)
boton.grid(row = 6, column = 1)

marco = tk.Frame(ventana,width=400, height=180, bd=1, relief="raised")
marco.grid(row=7, column =1)

ventana.mainloop()
