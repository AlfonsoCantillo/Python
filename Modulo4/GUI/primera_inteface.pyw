#Importar todas las clases de la libreria
from tkinter import *

raiz= Tk()
raiz.title("Mi primera ventana") #Titulo de la ventana
#raiz.resizable(False,False) #No permitir redimensionar la ventana. ancho x alto
raiz.iconbitmap("favicon.ico")
#raiz.geometry("800x600")
raiz.config(bg="blue")

#Crear Frame
miFrame= Frame()

miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="800",height="600")
miFrame.config(bd=5)
miFrame.config(relief="ridge")
miFrame.config(cursor="hand2")
#el método mainloop() muestra todo en pantalla y responde a la entrada del usuario hasta que el programa termina.
raiz.mainloop()