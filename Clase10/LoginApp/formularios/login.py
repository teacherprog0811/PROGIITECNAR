import tkinter as tk
import util.generic as utl
import util.db as db
from tkinter import messagebox
import json
import mysql.connector
from formularios.PAdmin import PAdmin
from formularios.PVentas import PVentas

class Login(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("INGRESO AL SISTEMA")
        self.resizable(False, False)
        utl.centrar_ventana(self, 800, 500)
        self.logo = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\logo.png", (300, 100))
        self.user = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\login.png", (48, 48))
        # frame_logo
        self.frame_logo = tk.Frame(self, bd=0, width=300,relief=tk.SOLID)
        self.frame_logo.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.llogo = tk.Label(self.frame_logo, image=self.logo)
        self.llogo.pack(padx=5, pady=150)

        # frame_form
        self.frame_form = tk.Frame(self, bd=0,relief=tk.SOLID).pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        self.texto=tk.Label(self.frame_form, text="INGRESO AL SISTEMA", font=('Times', 20))
        self.texto.pack(padx=10,pady=10)
        self.imglogin=tk.Label(self.frame_form, image=self.user)
        self.imglogin.pack(padx=10,pady=10)
        self.lusuario = tk.Label(self.frame_form,text="Usuario:",font=('Times', 14))
        self.lusuario.pack(padx=10, pady=5)
        self.cusuario = tk.Entry(self.frame_form, width=30,font=('Times', 12))
        self.cusuario.pack(fill=tk.X, padx=10, pady=10)
        self.cusuario.focus()

        self.lclave = tk.Label(self.frame_form,text="Clave:",font=('Times', 14))
        self.lclave.pack(fill=tk.X, padx=10, pady=5)

        self.cclave = tk.Entry(self.frame_form, width=30,font=('Times', 12), show="*")
        self.cclave.pack(fill=tk.X, padx=10, pady=10)

        self.bregistrar = tk.Button(self.frame_form, text="\uf082 Iniciar sesion", font=('Times', 16), command=self.validar)
        self.bregistrar.pack(fill=tk.X, padx=10, pady=10)

    def validar(self):
        
        sql="select * from Usuarios where Username='%s' and Clave = '%s'" % (self.cusuario.get(),self.cclave.get())
        db1 = db.Database()
        usuariologeado = db1.select(sql)
        if len(usuariologeado) == 0:
            messagebox.showerror('Error',"Usuario y/o clave incorrectos",parent=self)
        else:
            self.destroy()
            if usuariologeado[0][5] == "Administrador":
                PAdmin(usuariologeado[0][1],usuariologeado[0][2],usuariologeado[0][4])
            else:
                PVentas(usuariologeado[0][1],usuariologeado[0][2],usuariologeado[0][3])
    

        