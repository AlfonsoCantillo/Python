import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd

def cargar_csv():
  archivo = filedialog.askopenfilename(
    title="Seleccionar archivo CSV",
    filetypes=[("Archivos CSV", "*.csv")]
  )
  if archivo:
    df = pd.read_csv(archivo)
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, df.to_string())

def mostrar_mensaje():
  messagebox.showinfo("Mensaje", "Hola mundo")

ventana = tk.Tk()
ventana.title("Cargar CSV")
ventana.geometry("1024x760")
ventana.resizable(False, False)

ventana.config(bg="lightblue")


etiqueta = tk.Label(ventana, text="Seleccione un CSV:")
etiqueta.pack(pady=10)
boton = tk.Button(ventana, text="Haz Click ", command=cargar_csv)
boton.pack()

texto = tk.Text(ventana,wrap="none")
texto.pack(expand=True)

ventana.mainloop()
