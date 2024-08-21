import tkinter as tk
from tkinter import messagebox

def agregar_animal():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()

    if nombre != '' and precio != '':
        item = f"Mascota: {nombre}, Precio: {precio}, Pago: {pago}"
        if item not in lista_animales.get(0, tk.END):
            lista_animales.insert(tk.END, item)
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            metodo_pago.set("Contado")
        else:
            messagebox.showwarning(
                "Error", "Ya existe un animal con ese nombre.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del animal.")

def eliminar_animal():
    seleccionado = lista_animales.curselection()
    if seleccionado:
        lista_animales.delete(seleccionado)
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        metodo_pago.set("Contado")
    else:
        messagebox.showwarning(
            "Error", "Debes seleccionar un animal para eliminar.")

def actualizar_animal():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    pago = metodo_pago.get()

    if nombre != '' and precio != '':
        nuevo_item = f"Mascota: {nombre}, Precio: {precio}, Pago: {pago}"
        seleccionado = lista_animales.curselection()

        if seleccionado:
            lista_animales.delete(seleccionado)
            lista_animales.insert(seleccionado, nuevo_item)
        else:
            messagebox.showwarning(
                "Error", "Debes seleccionar un animal para actualizar.")
    else:
        messagebox.showwarning(
            "Error", "Debes ingresar el nombre y precio del animal.")

def obtener_datos_item(item):
    partes = item.split(", ")
    nombre = partes[0].split(": ")[1]
    precio = partes[1].split(": ")[1]
    pago = partes[2].split(": ")[1]
    return nombre, precio, pago

ventana = tk.Tk()
ventana.title("Tienda de Mascotas")
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

frame_datos = tk.Frame(ventana)
frame_datos.place(x=20, y=20)

label_nombre = tk.Label(frame_datos, text="Mascota:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(frame_datos)
entry_nombre.grid(row=0, column=1)

label_precio = tk.Label(frame_datos, text="Precio:")
label_precio.grid(row=1, column=0)
entry_precio = tk.Entry(frame_datos)
entry_precio.grid(row=1, column=1)
frame_datos.pack()

frame_pago = tk.Frame(ventana)
frame_pago.place(x=20, y=70)

metodo_pago = tk.StringVar(value="Contado")

label_pago = tk.Label(frame_pago, text="Método de pago:")
label_pago.pack()

radio_contado = tk.Radiobutton(
    frame_pago, text="Contado", variable=metodo_pago, value="Contado")
radio_contado.pack()

radio_credito = tk.Radiobutton(
    frame_pago, text="Crédito", variable=metodo_pago, value="Crédito")
radio_credito.pack()
frame_pago.pack()


frame_botones = tk.Frame(ventana)
frame_botones.place(x=20, y=130)

boton_agregar = tk.Button(
    frame_botones, text="Agregar", command=agregar_animal)
boton_agregar.pack()

boton_eliminar = tk.Button(
    frame_botones, text="Eliminar", command=eliminar_animal)
boton_eliminar.pack()

boton_actualizar = tk.Button(
    frame_botones, text="Actualizar", command=actualizar_animal)
boton_actualizar.pack()

frame_botones.pack()

frame_lista = tk.Frame(ventana)
frame_lista.place(x=20, y=220)

lista_animales = tk.Listbox(frame_lista, width=50, height=10)
lista_animales.pack()
frame_lista.pack()
ventana.mainloop()