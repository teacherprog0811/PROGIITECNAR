from tkinter import * 

master = Tk()
master.geometry("800x600")

# Creacion de labels
l1 = Label(master, text = "Nombre:")
l2 = Label(master, text = "Apellido:")

#Definiendo posiciones 
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# Creando cajas de texto con Entry
nombre = Entry(master)
apellido = Entry(master)

# Definiendo posisicones para cajas de texto
nombre.grid(row = 0, column = 1, pady = 4)
apellido.grid(row = 1, column = 1, pady = 4)

mainloop()
