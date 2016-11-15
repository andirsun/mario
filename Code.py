from tkinter import *
import time
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






posx = 0
posy = 0
limite = False
presionado = [0,0,0,0]
######
## defincion de funciones para los los botones en niveles "

def nivel1():
    ventanajuego.destroy()
    ventana1= Toplevel()
    ventana1.title("Juegonivel1")
    ventana1.geometry("760x520")
    canvas1= Canvas(ventana1, width=760, height=520)
    canvas1.pack()
    canvas1.create_image(0,0,anchor=NW,image=imgnivel1)
    Btnback1= Button(ventana1,text="VOLVER",font=("Agenci FB",13),command= ventana1.destroy).place(x=0,y=0)
    pj=canvas1.create_image(200,415,anchor=NW,image=megaman)

    ########$######
    def saltar():
        global ventana1,canvas1,pj,posx,posy,limite
        if(not limite):
            posy = posy - 10
        else:
            posy = posy + 10
        if(posy > -200 and not limite):
            canvas1.delete(pj)
            pj=canvas1.create_image(200,415,anchor=NW,image=megaman)
            ventana1.after(10,saltar)
        else:
            limite = True
            canvas1.delete(cuadrado)
            pj=canvas1.create_image(200,415,anchor=NW,image=megaman)
            if(posy != 0):
                ventana1.after(10,saltar)
        
    

    
    
    
    ventana1.mainloop()
def nivel2():
    ventanajuego.destroy()
    ventana2= Toplevel()
    ventana2.title("Juegonivel2")
    ventana2.geometry("800x600")
    fondonivel1= Label(ventana2,image=imgnivel1).place(x=0,y=0)
    Btnback1= Button(ventana2,text="VOLVER",font=("Agenci FB",13),command= ventana2.destroy).place(x=0,y=0)
    
    

    ventana2.mainloop()

def nivel3():
    ventanajuego.destroy()
    ventana3= Toplevel()
    ventana3.title("Juegonivel3")
    ventana3.geometry("800x600")
    fondonivel1= Label(ventana3,image=imgnivel1).place(x=0,y=0)
    Btnback1= Button(ventana3,text="VOLVER",font=("Agenci FB",13),command= ventana3.destroy).place(x=0,y=0)
    

    ventana3.mainloop()

def nivel4():
    ventanajuego.destroy()
    ventana4= Toplevel()
    ventana4.title("Juegonivel4")
    ventana4.geometry("800x600")
    fondonivel1= Label(ventana4,image=imgnivel1).place(x=0,y=0)
    Btnback1= Button(ventana4,text="VOLVER",font=("Agenci FB",13),command= ventana4.destroy).place(x=0,y=0)
    

    ventana4.mainloop()

def nivel5():
    ventanajuego.destroy()
    ventana5= Toplevel()
    ventana5.title("Juegonivel5")
    ventana5.geometry("800x600")
    fondonivel1= Label(ventana5,image=imgnivel1).place(x=0,y=0)
    Btnback1= Button(ventana5,text="VOLVER",font=("Agenci FB",13),command= ventana5.destroy).place(x=0,y=0)
    

    ventana5.mainloop()



######################################################
def Call(): # Definimos la funcion
    global ventanajuego
    ventanajuego= Toplevel()
    ventanajuego.geometry("894x506")
    fondoniveles= Label(ventanajuego,image=niveles).place(x=0,y=0)
    btnivel1= Button(ventanajuego,text="Principiante",font=("Agenci FB",13),command= nivel1).place(x=70,y=70)
    btnivel2= Button(ventanajuego,text="Novato",font=("Agenci FB",13),command= nivel2).place(x=85,y=200)
    btnivel3= Button(ventanajuego,text="Avanzado ",font=("Agenci FB",13),command=nivel3).place(x=70,y=330)
    btnivel4= Button(ventanajuego,text="Leyenda",font=("Agenci FB",13),command=nivel4).place(x=700,y=150)
    btnivel5= Button(ventanajuego,text="Invencible",font=("Agenci FB",13),command= nivel5).place(x=700,y=300)
    ventanajuego.mainloop()
#########################################    #########
def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño : Anderson laverde \n y codigo : Anderson laverde Gracia \n Contacto :  \n Pagina de Facebook : http://goo.gl/IwPKtl ")
########################################    
boton= Button(ventanamenu,text="JUGAR",font=("Agenci FB",13),command= Call).place(x=470,y=330)
boton2= Button(ventanamenu,text="CARGAR",font=("Agenci FB",13)).place(x=465,y=400)
boton3= Button(ventanamenu,text="CREDITOS",font=("Agenci FB",13),command=creditos).place(x=460,y=450)
boton4= Button(ventanamenu,text="SALIR",font=("Agenci FB",13),command=ventanamenu.destroy).place(x=480,y=490)
#########################################


























ventanamenu.mainloop() 
