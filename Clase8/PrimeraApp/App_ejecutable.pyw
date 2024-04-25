from tkinter import *
from PIL import Image, ImageTk # Requiere instalar Pillow 

ventana = Tk()
#Agregando icono a la ventana
path = Image.open("D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase8\PrimeraApp\imagenes\icono.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventana.title("Tecnar APP") 
# Establecemos el tamaño de la ventana.
ventana.geometry("1024x920")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Inicializamos la aplicacion
ventana.mainloop()