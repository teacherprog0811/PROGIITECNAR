import tkinter as tk 
from PIL import Image, ImageTk # Requiere instalar Pillow 

ventana = tk.Tk()
#Agregando icono a la ventana
path = Image.open("D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase8\PrimeraApp\imagenes\icono.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)
# Establecemos el nombre del titulo de la ventana.
ventana.title("Tecnar APP") 
# Establecemos el tamaño de la ventana. ventana.geometry("<ancho>x<alto>+<posición_x>+<posición_y>")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 
# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="gray")
# Inicializamos la aplicacion
ventana.mainloop()