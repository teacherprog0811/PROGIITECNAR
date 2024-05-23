import tkinter as tk
from tkinter import messagebox, ttk
import util.generic as utl
import util.db as db
import webbrowser
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
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\userinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\website.png", (32, 32))
        self.imglogout = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\logout.png", (32, 32))
        tk.Label(self.frame_user_info,image=self.usrimg).pack(padx=30,pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40,pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50,pady=4)
        tk.Button(self.frame_user_info,image=self.imgfacebook, command=self.abrirface).place(x=100,y=300)
        tk.Button(self.frame_user_info,image=self.imglinkedin, command=self.abrirlink).place(x=140,y=300)
        tk.Button(self.frame_user_info,image=self.imgwebsite, command=self.abrirweb).place(x=180,y=300)
        tk.Button(self.frame_user_info,image=self.imglogout, command=self.logout).place(x=220,y=300)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def main_usuarios(self):
        self.formulario_usuario()
        self.listar_usuarios()

    def formulario_usuario(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE USUARIOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font=('Times',14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=('Times',14))
        labelusuario.place(x=70,y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=40)
        self.cusuario.place(x=220,y=160)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=('Times',14))
        labelclave.place(x=500,y=100)
        self.cclave = tk.Entry(self.frame_dinamyc, width=40, show="*")
        self.cclave.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=500,y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame_dinamyc, text="Rol:", font=('Times',14))
        labeltipo.place(x=500,y=160)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=40, height=2)
        self.listatipo.place(x=600,y=160)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user)
        btnguardar.place(x=870, y=130)
    
    def listar_usuarios(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE USUARIOS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
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
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_user)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_user)
        btnupdate.place(x=200, y=520)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() =="" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" or self.tipo_user == "":
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
            if self.tipo_action == "Actualizar":
                sql2="update Usuarios set NombreCompleto='%s',Username='%s',Clave='%s',Correo='%s',Rol='%s' where Id=%s" % (self.cnombre.get(),self.cusuario.get(),self.cclave.get(),self.ccorreo.get(),self.tipo_user,self.ccedula.get())
                print(sql2)
                db2 = db.Database()
                db_users2 = db2.insert(sql2)
                if db_users2:
                    messagebox.showinfo('Info',"Usuario Actualizado con exito :-)",parent=self)
                    self.limpiar_panel(self.frame_dinamyc)
                else:
                    messagebox.showinfo('Error',"Ha habido un falla al intentar actualizar el registro :-( ",parent=self)
            else:
                sql="insert into Usuarios(Id,NombreCompleto,Username,Clave,Correo,Rol) values(%s,'%s','%s','%s','%s','%s')" % (self.ccedula.get(),self.cnombre.get(),self.cusuario.get(),self.cclave.get(),self.ccorreo.get(),self.tipo_user)
                db1 = db.Database()
                db_users = db1.insert(sql)
                if db_users:
                    messagebox.showinfo('Info',"Usuario registrado con exito :-)",parent=self)
                    self.limpiar_panel(self.frame_dinamyc)
                else:
                    messagebox.showinfo('Error',"Ha habido un falla al intentar guardar el registro :-( ",parent=self)

    def delete_user(self):
            idseleccionado = self.tablausuarios.item(self.tablausuarios.selection())["text"]
            sql1="delete from Usuarios where Id='%s'" % (idseleccionado)
            db2 = db.Database()
            db2.delete(sql1)
            messagebox.showinfo('Info',"Usuario eliminado con exito",parent=self)
            self.limpiar_panel(self.frame_dinamyc)



    def update_user(self):
        sql="select * from usuarios where Id=%s" % (self.tablausuarios.item(self.tablausuarios.selection())["text"])
        print(sql)
        db1 = db.Database()
        db_users = db1.select(sql)
        print (db_users)
        if len(db_users) == 0:
            messagebox.showerror('Error',"Usuario no encontrado",parent=self)
        else:
            self.ccedula.delete(0, tk.END)
            self.ccedula.insert(0, db_users[0][0])
            self.ccedula.config(state="disabled")
            self.cnombre.delete(0, tk.END)
            self.cnombre.insert(0,db_users[0][1])
            self.cusuario.delete(0, tk.END)
            self.cusuario.insert(0,db_users[0][2])
            self.cclave.delete(0, tk.END)
            self.cclave.insert(0,db_users[0][3])
            self.ccorreo.delete(0, tk.END)
            self.ccorreo.insert(0,db_users[0][4])
            self.tipo_action = "Actualizar"

    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
    def logout(self):
        self.destroy()

    def abrirface(self):
        url="https://www.facebook.com"
        webbrowser.open_new_tab(url)
    def abrirlink(self):
        url="https://www.linkedin.com"
        webbrowser.open_new_tab(url)
    def abrirweb(self):
        url= "https://itcloud.com.co"
        webbrowser.open_new_tab(url)        