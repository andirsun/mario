from tkinter import *
import time

## creacion de el primer canvas con la imagenes para el menu principal
ventanamenu= Tk()
ventanamenu.geometry("900x551")
ventanamenu.title("MarioMan")
##carga de todas la imagenes para la utilizacion despues 
fondo1= PhotoImage(file="fondoinicio.png")
imagenfondo= Label(ventanamenu,image=fondo1).place(x=0,y=0)
#fondo del juego
niveles = PhotoImage(file="niveles.png")
##### imagen para cada nivel
imgnivel1= PhotoImage(file="mapa.png")
megaman= PhotoImage(file="pjderecha.png")
megaman2= PhotoImage(file="pj2derecha.png")
malo1= PhotoImage(file="fantasma1.png")
malo2= PhotoImage(file="fantasma2.png")
malo3= PhotoImage(file="fantasma3.png")
malo4= PhotoImage(file="fantasma4.png")


###### prueba de variables para el salto
posx=200
posy=415
################## en esta funcion se definen los movimientos para el personaje principal y para los enemigos
def teclado(event):
    global canvas1,pj,posx,posy,pj2
    tecla = repr(event.char)
    if(tecla == "'a'"):
        canvas1.delete(pj)
        posx=posx-4
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        
        
        print("pos en x",posx,"pos en y",posy )
        #mundocontinuo
        if(posx<-60):
            canvas1.delete(pj)
            posx=posx+800
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
    if(tecla == "'d'"):
        canvas1.delete(pj)
        posx=posx+4
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        print("pos en x",posx,"pos en y",posy )
        #mundo continuo
        if(posx>742):
            canvas1.delete(pj)
            posx=posx-800
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        
            
    if(tecla=="'w'"):
        canvas1.delete(pj)
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        posy= posy-4
        if(posy<=-13):
            posy=posy+4
        elif(posx<280):
            posy=posy+4
        
        print("pos en x",posx,"pos en y",posy )
    if(tecla=="'s'"):
        canvas1.delete(pj)
        posy= posy+4
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        if(posy>415):
            posy=posy-4
        print("pos en x",posx,"pos en y",posy )


##### Prueba enemigo moviendoase
###pos para el primer enemigo
posxmalo1=20
posymalo1=50

        
        
        
    
        
               
        
        
        
            
        
        
        
            
            
    
    

    
                    
                
                

###### en esta funcion se definen los distintos ventanas y canvas para los niveles


def dificultad(event):
    global canvas1,pj,ventana1,enemigo1,pj2
    tecla = repr(event.char)
    if(tecla=="'q'"):      
        ventanajuego.destroy()
        ventana1= Toplevel()
        ventana1.title("Juegonivel1")
        ventana1.geometry("740x520")
        canvas1= Canvas(ventana1, width=760, height=520)
        canvas1.bind("<Key>", teclado)
        canvas1.pack()
        canvas1.focus_set()
        canvas1.create_image(0,0,anchor=NW,image=imgnivel1)
        Btnback1= Button(ventana1,text="VOLVER",font=("Agenci FB",13),command= ventana1.destroy).place(x=0,y=0)
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        pj2=canvas1.create_image(posx+900,posy,anchor=NW,image=megaman2)



    elif(tecla=="'w'"):      
        ventanajuego.destroy()
        ventana1= Toplevel()
        ventana1.title("Juegonivel1")
        ventana1.geometry("760x520")
        canvas1= Canvas(ventana1, width=760, height=520)
        canvas1.bind("<Key>", teclado)
        canvas1.pack()
        canvas1.focus_set()
        canvas1.create_image(0,0,anchor=NW,image=imgnivel1)
        Btnback1= Button(ventana1,text="VOLVER",font=("Agenci FB",13),command= ventana1.destroy).place(x=0,y=0)
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        pj2=canvas1.create_image(posx+900,posy,anchor=NW,image=megaman2)
        
        
        
        #enemigo2=canvas1.create_image(30,60,anchor=NW,image=malo2)
        #enemigo3=canvas1.create_image(40,70,anchor=NW,image=malo3)
        #enemigo4=canvas1.create_image(50,80,anchor=NW,image=malo4)
        
        ventana1.mainloop()

        

        #while (posxmalo< 1000):
        enemigo1=canvas1.create_image(posxmalo1,posymalo1,anchor=NW,image=malo1)
        #canvas1.delete(enemigo1)
            
            
            
        



        

        

         






    









######################################################
def Call(): # Definimos la funcion
    global ventanajuego
    ventanajuego= Toplevel()
    ventanajuego.geometry("900x506")
    canvas= Canvas(ventanajuego,width=894,height=506)
    canvas.create_image(0,0,anchor=NW,image=niveles)
    btnivel1= Button(ventanajuego,text="Si desea nivel FACIL Presionar Q",font=("Agenci FB",13)).place(x=70,y=70)
    btnivel2= Button(ventanajuego,text="Si desea nivel NORMAL  Presionar W",font=("Agenci FB",13)).place(x=70,y=100)
    btnivel3= Button(ventanajuego,text="Si desea nivel MEDIO  Presionar E",font=("Agenci FB",13)).place(x=70,y=130)
    btnivel4= Button(ventanajuego,text="Si desea nivel FRIKASO Presionar R",font=("Agenci FB",13)).place(x=70,y=160)
    btnivel5= Button(ventanajuego,text="Si desea nivel IMPOSIBLEEE Presionar T",font=("Agenci FB",13)).place(x=70,y=190)
    canvas.pack()
    canvas.focus_set()
    canvas.bind("<Key>", dificultad)
    ventanajuego.mainloop()
#########################################    #########
def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño : Anderson laverde \n y codigo : Anderson laverde Gracia \n Contacto :  \n Pagina de Facebook : http://goo.gl/IwPKtl ")
########################################    
boton= Button(ventanamenu,text="MAMA HUEVOOOO",font=("Agenci FB",13),command= Call,bg="#0080FF",cursor="crosshair",relief="groove",activebackground="#F50743").place(x=440,y=340)
boton2= Button(ventanamenu,text="CARGAR",font=("Agenci FB",13),bg="#FF3333",cursor="dotbox",relief="groove",activebackground="#F50743").place(x=435,y=390)
boton3= Button(ventanamenu,text="CREDITOS",font=("Agenci FB",13),command=creditos,bg="#0080FF",cursor="fleur",relief="groove",activebackground="#F50743").place(x=430,y=440)
boton4= Button(ventanamenu,text="SALIR",font=("Agenci FB",13),command=ventanamenu.destroy,bg="#FF3333",cursor="pirate",relief="groove",activebackground="#F50743").place(x=448,y=490)
#########################################


























ventanamenu.mainloop() 
