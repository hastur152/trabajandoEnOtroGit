from tkinter import *
from PIL import ImageTk, Image
root = Tk()

miFrame = Frame()

miFrame.pack(fill="both", expand=1)
miFrame.config(width=650, height=650)

miFrame.config(bg="cyan")

miLabel = Label(miFrame, text="hola sergio sos un crack",
                bg="cyan", font=("Comic Sans MS", 18), fg="grey")
miImagen = ImageTk.PhotoImage(Image.open(r"/home/sergioleon/Escritorio/python LA MEJOR PARTE DEL CURSOI/GIU/imagenes/png/ojo.jpg")) #si le paso la ruta relavitvano funcionara toca pasarle la completa
milabel2 = Label(miFrame, image=miImagen).place(x=200, y=100)
miLabel.place(x=100, y=200)


root.mainloop()
