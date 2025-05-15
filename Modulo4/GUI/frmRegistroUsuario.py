from tkinter import *
from tkinter import messagebox

def registrar_usuario():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    email = entry_email.get()
    contrasena = entry_contrasena.get()
    confirmar = entry_confirmar.get()

    if not all([nombre, apellido, email, contrasena, confirmar]):
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    if contrasena != confirmar:
        messagebox.showerror("Error de contraseña", "Las contraseñas no coinciden.")
        return

    # Aquí podrías guardar en una base de datos o archivo
    messagebox.showinfo("Registro exitoso", f"Usuario {nombre} {apellido} registrado.")

    limpiar_formulario()

def limpiar_formulario():
    entry_nombre.delete(0, END)
    entry_apellido.delete(0, END)
    entry_email.delete(0, END)
    entry_contrasena.delete(0, END)
    entry_confirmar.delete(0, END)

# Ventana principal
raiz = Tk()
raiz.title("Formulario de Registro")
raiz.geometry("400x300")
raiz.resizable(False, False)

# Etiquetas y campos
Label(raiz, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky=E)
entry_nombre = Entry(raiz)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

Label(raiz, text="Apellido:").grid(row=1, column=0, padx=10, pady=5, sticky=E)
entry_apellido = Entry(raiz)
entry_apellido.grid(row=1, column=1, padx=10, pady=5)

Label(raiz, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=E)
entry_email = Entry(raiz)
entry_email.grid(row=2, column=1, padx=10, pady=5)

Label(raiz, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5, sticky=E)
entry_contrasena = Entry(raiz, show="*")
entry_contrasena.grid(row=3, column=1, padx=10, pady=5)

Label(raiz, text="Confirmar:").grid(row=4, column=0, padx=10, pady=5, sticky=E)
entry_confirmar = Entry(raiz, show="*")
entry_confirmar.grid(row=4, column=1, padx=10, pady=5)

# Botón registrar
btn_registrar = Button(raiz, text="Registrar", command=registrar_usuario)
btn_registrar.grid(row=5, column=0, columnspan=2, pady=20)

raiz.mainloop()
