from tkinter import *

raiz = Tk()
#raiz.resizable(False,False)
raiz.geometry("500x400")
raiz.title("Registro de usuarios")
raiz.config(bg="lightblue")

frmLogo = Frame(raiz,
                width=200,
                height=200,
                bg="red"
              )
frmLogo.pack()
frmLogo.pack_propagate(False)


imgLogo=PhotoImage(file="logo_saeta.png")
Label(frmLogo, image=imgLogo,bg="lightblue").place(relx=0.5, rely=0.5, anchor="center")

"""Label(raiz, 
      text="Nombres:",
      bg="lightblue",
      font=("Tahoma", 10, "bold"),
      justify="left"
    ).grid(row=1, column=0, padx=10, pady=5, sticky=E)

Label(raiz, text="Apellidos:",bg="lightblue",font=("Tahoma", 10, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky=E)
"""
raiz.mainloop()