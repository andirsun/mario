from tkinter import *        
## creacion de el primer canvas con la imagenes para el menu principal
ventanamenu= Tk()
ventanamenu.geometry("977x551")
ventanamenu.title("MarioMan")

fondo1= PhotoImage(file="FONDO1.png")
imagenfondo= Label(ventanamenu,image=fondo1).place(x=0,y=0)
#fondo del juego
niveles = PhotoImage(file="niveles.png")
#####
##### imagen para cada nivel
imgnivel1= PhotoImage(file="mapa.png")
megaman= PhotoImage(file="megaman.png") 

######
## defincion de funciones para los los botones en niveles "

def nivel1():
    ventana1= Toplevel()
    ventana1.title("Juegonivel1")
    ventana1.geometry("760x520")
    fondonivel1= Label(ventana1,image=imgnivel1).place(x=0,y=0)
    pj1= Label(ventana1,image=megaman).place(x=200,y=400)
    if event.keysym=='Up':
        print("hello")
    ventana1.mainloop
def nivel2():
    ventana2= Toplevel()
    ventana2.title("Juegonivel2")
    ventana2.geometry("800x600")
    

    ventana2.mainloop

def nivel3():
    ventana3= Toplevel()
    ventana3.title("Juegonivel3")
    ventana3.geometry("800x600")

    ventana3.mainloop

def nivel4():
    ventana4= Toplevel()
    ventana4.title("Juegonivel4")
    ventana4.geometry("800x600")

    ventana4.mainloop

def nivel5():
    ventana5= Toplevel()
    ventana5.title("Juegonivel5")
    ventana5.geometry("800x600")

    ventana5.mainloop
######################################################
def Call(): # Definimos la funcion
    ventanajuego= Toplevel()
    ventanajuego.geometry("894x506")
    fondoniveles= Label(ventanajuego,image=niveles).place(x=0,y=0)
    btnivel1= Button(ventanajuego,text="Principiante",font=("Agenci FB",13),command= nivel1).place(x=70,y=70)
    btnivel2= Button(ventanajuego,text="Novato",font=("Agenci FB",13),command= nivel2).place(x=85,y=200)
    btnivel3= Button(ventanajuego,text="Avanzado ",font=("Agenci FB",13),command=nivel3).place(x=70,y=330)
    btnivel4= Button(ventanajuego,text="Leyenda",font=("Agenci FB",13),command=nivel4).place(x=700,y=150)
    btnivel5= Button(ventanajuego,text="Invencible",font=("Agenci FB",13),command= nivel5).place(x=700,y=300)
    ventanajuego.mainloop
#########################################    #########
def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño y codigo : Anderson laverde")
########################################    
boton= Button(ventanamenu,text="JUGAR",font=("Agenci FB",13),command= Call).place(x=470,y=330)
boton2= Button(ventanamenu,text="CARGAR",font=("Agenci FB",13)).place(x=465,y=400)
boton3= Button(ventanamenu,text="CREDITOS",font=("Agenci FB",13),command=creditos).place(x=460,y=450)
boton4= Button(ventanamenu,text="SALIR",font=("Agenci FB",13),command=ventanamenu.destroy).place(x=480,y=490)
#########################################3


























ventanamenu.mainloop() 
