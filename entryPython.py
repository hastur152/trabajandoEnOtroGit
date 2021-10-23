from tkinter import *
import tkinter.scrolledtext as scrolledtext


# VENTA
root = Tk()
root.title("entry")
root.config(bg="cyan")
# root.iconbitmap(r"GIU/imagenes/ico/camara.ico")
# LAMINA
miFrame = Frame(root)
miFrame.config(width=600, height=300)
miFrame.config(bg="cyan")
miFrame.pack(fill="both", expand=1)
# COMPONENTES
# componentes nombre
minombre = StringVar()
nombreLabel = Label(miFrame, text="nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
cuadroTexto = Entry(miFrame, textvariable=minombre)
cuadroTexto.grid(row=0, column=1)
cuadroTexto.config(fg="blue")


# componentes apelllido
apellidoLabel = Label(miFrame, text="apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)
cuadroTexto1 = Entry(miFrame, fg="red")
cuadroTexto1.grid(row=1, column=1)
cuadroTexto1.config(fg="red")
# componentes direccion
nombreLabel = Label(miFrame, text="direccion: ")
nombreLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)
cuadroTexto2 = Entry(miFrame, fg="red")
cuadroTexto2.grid(row=2, column=1)
cuadroTexto2.config(fg="green")
# componente de contraseña
cuadroContra = Entry(miFrame, fg="red")
contraLabel = Label(miFrame, text="contraseña: ")
cuadroContra.config(show="*")
cuadroContra.grid(row=3, column=1, sticky="w", padx=10, pady=10)
contraLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)
# AGREGANDO BOTONES


def codigoBoton():
    minombre.set("sergio")


boton_envio = Button(root, text="enviar", command=codigoBoton)
boton_envio.pack()


# cuadro de texto
comentarioLabel = Label(miFrame, text="comentario: ")
comentarioLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)
# se puede hacer de esa manera pero la mejor es importando tkinter.scolledtext as scrolledtext y creando la caja de texto  osea de esta manera
caja_texto_con_scroll = scrolledtext.ScrolledText(miFrame)
caja_texto_con_scroll.config(width=20, height=5)
caja_texto_con_scroll.grid(row=4, column=1)

# crando cuadro de texto con scrollbar de la manera largo mejor la que tengo ahora
"""#texto_comentario = Text(miFrame, width=20, height=5)
#texto_comentario.grid(row=4, column=1, pady=10, padx=10)
# cuadrotexto_comentario.config(fg="green")
# creando el scroll bar de mi text area podemos seleccionar tambien el tipo de scroll sui es vertical o horozintal por eso pusimos yview
scrollVert = Scrollbar(miFrame, command=texto_comentario.yview)
# despues de crear e scrollbar lo tenemos que colocar usando el grid
# entonces para ponerla la ponemos en el grid como le acabamos de indicar
scrollVert.grid(row=4, column=2)"""


root.mainloop()
