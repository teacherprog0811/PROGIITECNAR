import tkinter as tk


class PAdmin():
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.title("Panel Administrativo")
        self.windows.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.windows.winfo_screenwidth() #método para obtener Ancho
        alto_pantalla = self.windows.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.windows.geometry(f"{ancho_pantalla}x{alto_pantalla}")
       # logo = utl.leer_imagen("D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPO\Clase9\LoginApp\imagenes\logo.png", (300, 100))

        # frame_menu_lateral
        frame_menu_lateral = tk.Frame(self.windows, bd=0, width=300,relief=tk.SOLID)
        frame_menu_lateral.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        menu=tk.Label(frame_menu_lateral, text="MENU", font=('Times', 20))
        menu.pack(padx=10,pady=30)


        # frame_panel_informativo
        frame_panel_informativo = tk.Frame(self.windows, bd=0,relief=tk.SOLID)
        frame_panel_informativo.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        texto=tk.Label(frame_panel_informativo, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=10,pady=30)

        self.windows.mainloop()