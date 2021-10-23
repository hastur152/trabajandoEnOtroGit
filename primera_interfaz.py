from tkinter import *

raiz = Tk()

raiz.title("mi primera ventana")

raiz.resizable(True, 0)

# raiz.iconbitmap("@GIU/imagenes/xpm/leon.xbm")PREGUNTAR A ALGUIEN COMO PONER EN LINUX UN ICONO A LA VENTANA


# raiz.geometry("650x350")#la aiz siemrpre se adaptara la tamaño del ontenedor inerno

raiz.config(bg="cyan")
raiz.config(bd=45)
raiz.config(relief="groove")

miFrame = Frame()

# fill es que cuadno redimenzionemos la ventana se llene segun donde queramos osea en y o x o both para ambos lados
miFrame.pack(fill="both", expand="True")
# TODAS LAS COSAS QUE HEMOS APLICADO A EL FRAME SE LE PUEDE APLICAR ALA VENTANA
miFrame.config(bg="red")
# le da el tamaño de sombrado o bordes redodndas que tendra que tener el relief
miFrame.config(bd=30)

# con esta le cambiamos el tipo de borde a las horillas del frame se puede ver cuando no tenemos la opcion de rellenar
miFrame.config(relief="sunken")
# para cambiar el tipo de cursor tambien podemos
miFrame.config(cursor="pirate")

miFrame.config(width=650, height=300)


raiz.mainloop()
