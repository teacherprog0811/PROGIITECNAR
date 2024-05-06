import tkinter as tk
import util.generic as utl


ventana = tk.Tk()

variablesexo = tk.IntVar()

ventana.title("TECNAR LOGIN")

utl.centrar_ventana(ventana, 800, 500)
ventana.resizable(False,False)
logo = utl.leer_imagen("D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase8\LoginApp\imagenes\logo.png", (300, 100))

# frame_logo
frame_logo = tk.Frame(ventana, bd=0, width=300,relief=tk.SOLID, padx=10, pady=10, bg="#F4F5F7")
frame_logo.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
label = tk.Label(frame_logo, image=logo, bg="#F4F5F7")
label.place(x=0, y=0, relwidth=1, relheight=1)

# frame_form

# frame_form
frame_form = tk.Frame(ventana, bd=0,relief=tk.SOLID, bg="#F4F5F7").pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

# frame_form_top
frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg="#F4F5F7")
frame_form_top.pack(side="top", fill=tk.X)
title = tk.Label(frame_form_top, text="Login", font=('Times', 30), fg="black", bg="#F4F5F7", pady=50).pack(expand=tk.YES, fill=tk.BOTH)
# end frame_form_top

# frame_form_fill
frame_form_fill = tk.Frame(frame_form, height=50,  bd=0, relief=tk.SOLID, bg="#F4F5F7").pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)

lusuario = tk.Label(frame_form_fill,text="Usuario:",font=('Times', 18), fg="black", anchor="w").pack(fill=tk.X, padx=30, pady=5)
cusuario = tk.Entry(frame_form_fill, width=30,font=('Times', 18)).pack(fill=tk.X, padx=30, pady=10)

lclave = tk.Label(frame_form_fill,text="Clave:",font=('Times', 18), fg="black", anchor="w").pack(fill=tk.X, padx=30, pady=5)

cclave = tk.Entry(frame_form_fill, width=30,font=('Times', 18)).pack(fill=tk.X, padx=30, pady=10)

bregistrar = tk.Button(frame_form_fill, text="Iniciar sesion").pack(fill=tk.X, padx=20, pady=20)

ventana.mainloop()