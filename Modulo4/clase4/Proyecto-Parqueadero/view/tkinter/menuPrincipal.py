import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from controller.vehiculosController import vehiculosController
from PIL import Image
from customtkinter import CTkImage


class MenuPrincipal:
    def __init__(self):
        self.vehiculosController = vehiculosController()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.ventana = ctk.CTk()
        self.ventana.title("Menu Principal")
        #self.ventana.state("zoomed")
        self.ventana.update_idletasks()
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{screen_width}x{screen_height}+0+0")        
        self.ventana.resizable(False, True)

        # Configurar filas y columnas de la ventana para que se expandan
        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(0, weight=1)

        # Título centrado arriba
        titulo = ctk.CTkLabel(self.ventana, text="Sistema de Control y Gestión de Parqueadero", font=("Tahoma", 30))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame principal con 2 columnas: tabla y botones
        frame_contenido = ctk.CTkFrame(self.ventana,fg_color="transparent")
        frame_contenido.grid(row=1, column=0, padx=40, pady=20, sticky='nsew')
        frame_contenido.grid_columnconfigure(0, weight=3)  # columna para tabla
        frame_contenido.grid_columnconfigure(1, weight=1)  # columna para botones
        
        # Frame: tabla
        self.frame_tabla = ctk.CTkFrame(frame_contenido,fg_color="transparent")
        self.frame_tabla.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        # Frame: botones
        self.frame_botones = ctk.CTkFrame(frame_contenido,fg_color="transparent")
        self.frame_botones.grid(row=0, column=1, sticky="n")

        # Estilos de la tabla
        self.columnas = ('placa', 'tipoVehiculo', 'fechaIngreso')
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", background="lightblue", foreground="black", font=("Tahoma", 12, "bold"))
        self.style.configure("Treeview", background="white", foreground="black", rowheight=25, font=("Tahoma", 10))

        # Tabla Treeview
        self.tabla = ttk.Treeview(self.frame_tabla, columns=self.columnas, show='headings')
        self.tabla.heading('placa', text='Placa')
        self.tabla.heading('tipoVehiculo', text='Tipo Vehículo')
        self.tabla.heading('fechaIngreso', text='Fecha / Hora Ingreso')

        self.tabla.column('placa', width=150, anchor='center')
        self.tabla.column('tipoVehiculo', width=150, anchor='center')
        self.tabla.column('fechaIngreso', width=300, anchor='center')
        self.tabla.pack(fill='both', expand=True)

        icono_ingresar = CTkImage(Image.open("src/iconos/add-car.png"), size=(32, 32))
        icono_liquidar = CTkImage(Image.open("src/iconos/delete-car.png"), size=(32, 32))
        #tk.PhotoImage(file="src/iconos/guardar.png")

        # Botones en el frame lateral
        btn_ingresar = ctk.CTkButton(
            self.frame_botones, 
            text="Ingresar Vehículo", 
            command=self.ingresar_vehiculo, 
            font= ("Tahoma", 12, "bold"),
            width=200,
            height=40,
            image=icono_ingresar,
            compound="left",
            fg_color="#2196F3",      
            hover_color="#1976D2", 
            text_color="white",
          )
        btn_ingresar.pack(pady=10)

        btn_liquidar = ctk.CTkButton(
            self.frame_botones, 
            text="Liquidar Salida", 
            command=self.liquidar_salida,
            font= ("Tahoma", 12, "bold"), 
            width=200,
            height=40,
            image=icono_liquidar,
            compound="left",
            fg_color="#2196F3",      
            hover_color="#1976D2", 
            text_color="white",
          )
        btn_liquidar.pack(pady=10)

        self.llenar_tabla()
        self.ventana.mainloop()

    def llenar_tabla(self):
        df = self.vehiculosController.obtener_vehiculos_todos()
        vehiculos = df.to_dict('records')
        for vehiculo in vehiculos:
            fecha_str = vehiculo['fechaIngreso']
            fecha = fecha_str  # si ya es string, úsala directamente
            self.tabla.insert('', 'end', values=(vehiculo['placa'], vehiculo['tipoVehiculo'], fecha))

    def ingresar_vehiculo(self):
        print("Ingresar vehículo...")

    def liquidar_salida(self):
        print("Liquidar salida...")

