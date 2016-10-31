from tkinter import * 
        
## creacion de el primer canvas con la imagenes para el menu principal

ventana1= Tk()
ventana1.geometry("977x551")
ventana1.title("MarioMan")

fondo1= PhotoImage(file="FONDO1.png")
imagenfondo= Label(ventana1,image=fondo1).place(x=0,y=0)
#fondo del juego
fondojuego= PhotoImage(file="mapa.png")




#Botones  de inicio de juego con sus funciones respecto a que va hacer cada boton 

def Call(): # Definimos la funcion
    ventanajuego=Tk()
    ventanajuego.geometry("800x600")
    ventanajuego.title("JUEGO MARIO MAN BY ANDER DEVELOPER")
    imgfonjuego= Label(ventanajuego,image=fondojuego).place(x=0,y=0)
    botonjuego= Button(ventanajuego,text="jajajaja").place(x=400,y=300)
    ventanajuego.mainloop()


def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño y codigo : Anderson laverde")

imgbotoninicio= PhotoImage("boton.gif")
boton= Button(ventana1,text="JUGAR",font=("Agenci FB",13),command= Call,).place(x=470,y=350)
boton2= Button(ventana1,text="CARGAR",font=("Agenci FB",13)).place(x=465,y=390)
boton3= Button(ventana1,text="CREDITOS",font=("Agenci FB",13),command=creditos).place(x=460,y=430)
boton4= Button(ventana1,text="SALIR",font=("Agenci FB",13),command=ventana1.destroy).place(x=480,y=470)


























ventana1.mainloop() 
