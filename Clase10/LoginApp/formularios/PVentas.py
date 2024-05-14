import tkinter as tk
import json
from tkinter import messagebox
import util.generic as utl
class PVentas(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Ventas")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Crear Cliente", command=self.crear_cliente_form)  
        menuclientes.add_command(label="Listar Clientes")  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Crear Venta")  
        menuventas.add_command(label="Listar Ventas")  
        menubar.add_cascade(label="Ventas", menu=menuventas)

        self.config(menu=menubar)

        # frame user info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL VENTAS", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        usrimg = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\userinfo.png", (48, 48))
        imgusr=tk.Label(self.frame_user_info, image=usrimg)
        imgusr.pack(padx=30,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.name, font=('Times', 14))
        texto1.pack(padx=40,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.email, font=('Times', 14))
        texto1.pack(padx=50,pady=4)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def crear_cliente_form(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE CLIENTES", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=220, y=130)

        labeldireccion = tk.Label(self.frame_dinamyc,text="Direccion:", font=('Times',14))
        labeldireccion.place(x=70,y=160)
        self.cdireccion = tk.Entry(self.frame_dinamyc, width=80)
        self.cdireccion.place(x=220,y=160)

        labeltelefono = tk.Label(self.frame_dinamyc,text="Telefono:", font=('Times',14))
        labeltelefono.place(x=70,y=190)
        self.ctelefono = tk.Entry(self.frame_dinamyc, width=80)
        self.ctelefono.place(x=220, y=190)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo", font=('Times',14))
        labelcorreo.place(x=70,y=220)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=220, y=220)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_client)
        btnguardar.place(x=220, y=280)
    
    def save_client(self):
        messagebox.showinfo('Info',"Usuario registrado con exito",parent=self)
        self.limpiar_panel(self.frame_dinamyc)
    
    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()