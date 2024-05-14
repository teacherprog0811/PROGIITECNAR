import tkinter as tk
import json
from tkinter import messagebox, ttk, PhotoImage
import util.generic as utl
import util.db as db


class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  
        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Crear Usuario", command=self.crear_usuario_form)  
        menuuser.add_command(label="Listar Usuarios", command=self.listar_usuarios) 
        menubar.add_cascade(label="Usuarios", menu=menuuser)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Crear Cliente")  
        menuclientes.add_command(label="Listar Clientes")  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Crear Venta")  
        menuventas.add_command(label="Listar Ventas")  
        menubar.add_cascade(label="Ventas", menu=menuventas)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Crear Categoria")  
        menucategorias.add_command(label="Listar Categarias")  
        menubar.add_cascade(label="Categorias", menu=menucategorias)   

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Crear Producto")  
        menuproducto.add_command(label="Listar Productos")  
        menubar.add_cascade(label="Ventas", menu=menuproducto)   

        self.config(menu=menubar)

        # frame user info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        usrimg = PhotoImage(file=r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\userinfo.png")
        imgusr=tk.Label(self.frame_user_info,image=usrimg)
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
        #textobienvenida=tk.Label(self.frame_dinamyc, text="DINAMICO", font=('Times', 20))
        #textobienvenida.pack(padx=20,pady=4)

    def crear_usuario_form(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE USUARIOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font=('Times',14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=80)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=80)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=('Times',14))
        labelusuario.place(x=70,y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=80)
        self.cusuario.place(x=220,y=160)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=('Times',14))
        labelclave.place(x=70,y=190)
        self.cclave = tk.Entry(self.frame_dinamyc, width=80, show="*")
        self.cclave.place(x=220, y=190)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=70,y=220)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=80)
        self.ccorreo.place(x=220, y=220)

        labeltipo = tk.Label(self.frame_dinamyc, text="Tipo:")
        labeltipo.place(x=70,y=250)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=80, height=2)
        self.listatipo.place(x=220,y=250)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user)
        btnguardar.place(x=220, y=300)
    
    def listar_usuarios(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE USUARIOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=70)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        sql="select * from Usuarios"
        db1 = db.Database()
        db_users = db1.select(sql)
        for usuarios in db_users:
            self.tablausuarios.insert("", "end", text=f'{usuarios[0]}',values=(f'{usuarios[1]}',f'{usuarios[2]}',f'{usuarios[4]}', f'{usuarios[5]}'))
        self.tablausuarios.place(x=70, y=100)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)

        sql="insert into Usuarios(Id,NombreCompleto,Username,Clave,Correo,Rol) values(%s,'%s','%s','%s','%s','%s')" % (self.ccedula.get(),self.cnombre.get(),self.cusuario.get(),self.cclave.get(),self.ccorreo.get(),self.tipo_user)
        print(sql)
        db1 = db.Database()
        db_users = db1.insert(sql)
        if db_users:
            messagebox.showinfo('Info',"Usuario registrado con exito :-)",parent=self)
            self.limpiar_panel(self.frame_dinamyc)
        else:
            messagebox.showinfo('Error',"Ha habido un falla al intentar guardar el registro :-( ",parent=self)

    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()        