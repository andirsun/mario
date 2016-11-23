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
instrucciones= PhotoImage(file="instrucciones.png")
imgnivel1= PhotoImage(file="mapa.png")
megaman= PhotoImage(file="megaman1.png")
megaman2= PhotoImage(file="megaman2.png")
megaman3= PhotoImage(file="megaman3.png")
megamanderecha= PhotoImage(file="megamanderecha1.png")
megamanderecha2= PhotoImage(file="megamanderecha2.png")
megamanderecha3= PhotoImage(file="megamanderecha3.png")


mario= PhotoImage(file="mario1.png")
mario2= PhotoImage(file="mario2.png")
marioizquierda= PhotoImage(file="marioizquierda1.png")
marioizquierda2= PhotoImage(file="marioizquierda2.png")
malo1= PhotoImage(file="hongoizquierda.png")
malo1d=PhotoImage(file="hongoderecha.png")


malo2= PhotoImage(file="fantasma2.png")
malo3= PhotoImage(file="fantasma3.png")
malo4= PhotoImage(file="fantasma4.png")





###### posicion de megaman
posx=200
posy=440
################posicion mario inicial
posxm=700
posym=440

posxmalo=100
posymalo=100

posxmalo2=700
posymalo2=100

#####posicion para el salto

####estados para el uso y cambio de imagenes 
estadomega=0
estadomegaderecha=0
estadomario=0
estadomarioizquierda=0
        
     
    
################## en esta funcion se definen los movimientos para el personaje principal y para los enemigos
def teclado(event):
    """
    Requerimiento luego 
    """
    global canvas1,pj,posx,posy,pj2,estadomegaderecha,estadomega,estadomarioizquierda,estadomario,posxm,posym
    tecla = repr(event.char)
    if(tecla == "'a'" ):
        #print("pos en x",posx,"pos en y",posy )
        ##mundoparalelo
        if(posx<-60):
            canvas1.delete(pj)
            posx=posx+800
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
            
       ########     #####
        if(estadomegaderecha==0):
            canvas1.delete(pj)
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megamanderecha2)       
            posx=posx-4
            estadomegaderecha=1
        elif(estadomegaderecha==1):
            canvas1.delete(pj)
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megamanderecha3)       
            posx=posx-4
            estadomegaderecha=0
            
            
            
        
            
   
        
        
    if(tecla == "'d'" ):
        
        #print("pos en x",posx,"pos en y",posy )
        #mundo continuo
        if(posx>742):
            canvas1.delete(pj)
            posx=posx-800
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
            ##### cambios de imagen 
    
        if(estadomega==0):
            canvas1.delete(pj)
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman2)       
            posx=posx+4
            estadomega=1
        elif(estadomega==1):
            canvas1.delete(pj)
            pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman3)       
            posx=posx+4
            estadomega=0
        
    
        
            
    if(tecla=="'w'"):
        canvas1.delete(pj)
        posy= posy-4
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        
        
        if(posy<=387 and posy>=299 and posx<=276 ):   ## escalones de abajo control de choque
            posy=posy+4
        elif(posy<=387 and posy>=299 and posx>=404 ):   ## escalones de abajo control de choque
            posy=posy+4
        elif(posy<=283 and posy>=199 and posx<=92 ):   ## escalones de medio izquierda control de choque
            posy=posy+4
        elif(posy<=283 and posy>=199 and posx>=588 ):   ## escalones de medio derecha control de choque
            posy=posy+4
        elif(posy<=267 and posy>=176 and posx>=124 and posx<=556 ):   ## choque escalon medio 
            posy=posy+4
        elif(posy<=143 and posy>=59 and posx<=324 ):  # choque escalon arriba izquierda 
            posy=posy+4
        elif(posy<=143 and posy>=59 and posx>=360):   # choque escalon arriba derecha 
            posy=posy+4
        
        
        
        print("pos en x",posx,"pos en y",posy )
    if(tecla=="'s'"):
        canvas1.delete(pj)
        posy= posy+4
        pj=canvas1.create_image(posx,posy,anchor=NW,image=megaman)
        
        

        ###### posiciones para control de choque 
        if(posy<=387 and posy>=299 and posx<=276): # choque primer escalon abajo izquierda
            posy=posy-4
        elif(posy<=387 and posy>=299 and posx>=404): # choque primer escalon abajo derecha
            posy=posy-4
        elif(posy<=283 and posy>=199 and posx<=92): # choque escalon medio izquierda
            posy=posy-4
        elif(posy<=283 and posy>=199 and posx>=588): # choque escalon medio derecha
            posy=posy-4
        elif(posy<=267 and posy>=176 and posx>=124 and posx<=556 ): # CHOQUE escalon medio 
            posy=posy-4
        elif(posy<=143 and posy>=59 and posx<=324):    # choque escalon arriba izquierda 
            posy=posy-4
        elif(posy<=143 and posy>=59 and posx>=360):    # choque escalon arriba derecha 
            posy=posy-4 
        elif (posy>=419): # que no pase del piso 
            posy=posy-4
        print("pos en x",posx,"pos en y",posy )




#############################################################
    if(tecla=="'j'"):
        if(posxm<-60):
            canvas1.delete(pj2)
            posxm=posxm+800
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)
            
       ########     #####
        if(estadomarioizquierda==0):
            canvas1.delete(pj2)
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)       
            posxm=posxm-4
            estadomarioizquierda=1
        elif(estadomarioizquierda==1):
            canvas1.delete(pj2)
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario2)       
            posxm=posxm-4
            estadomarioizquierda=0




    if(tecla == "'l'"):
        #mundo continuo
        if(posxm>742):
            canvas1.delete(pj2)
            posxm=posxm-800
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=marioizquierda)
        
            ##### cambios de imagen 
    
        if(estadomario==0):
            canvas1.delete(pj2)
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=marioizquierda)       
            posxm=posxm+4
            estadomario=1
        elif(estadomario==1):
            canvas1.delete(pj2)
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=marioizquierda2)       
            posxm=posxm+4
            estadomario=0
       # print("posxm",posxm,"posym",posym)


        if(tecla=="'i'"):
            canvas1.delete(pj2)
            posym= posym-4
            pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)
            print("presiono tecla")
        
        
        if(posym<=387 and posym>=299 and posxm<=276 ):   ## escalones de abajo control de choque
            posym=posym+4
        elif(posym<=387 and posym>=299 and posxm>=404 ):   ## escalones de abajo control de choque
            posym=posym+4
        elif(posym<=283 and posym>=199 and posxm<=92 ):   ## escalones de medio izquierda control de choque
            posym=posym+4
        elif(posym<=283 and posym>=199 and posxm>=588 ):   ## escalones de medio derecha control de choque
            posym=posym+4
        elif(posym<=267 and posym>=176 and posxm>=124 and posxm<=556 ):   ## choque escalon medio 
            posym=posym+4
        elif(posym<=143 and posym>=59 and posxm<=324 ):  # choque escalon arriba izquierda 
            posym=posym+4
        elif(posym<=143 and posym>=59 and posxm>=360):   # choque escalon arriba derecha 
            posym=posym+4


    
        
        


##### Prueba enemigo moviendoase
###pos para el primer enemigo



def mover1():
    """ 
    funcion que realiza el movimiento de el primer enemigo
    """

    global posxmalo,posymalo,malo,ventana1,canvas1
    canvas1.delete(malo)
    malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    posxmalo=posxmalo+4
    #print(posxmalo, "posymalo",posymalo)
    if(posxmalo>742):
        canvas1.delete(malo)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        posxmalo=posxmalo-800
    if(posxmalo==320 and posymalo==100):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==540 and posymalo==220):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==300 and posymalo==340):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    if(posxmalo>670 and posymalo==460):
        canvas1.delete(malo)
        posxmalo=100
        posymalo=100
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    ventana1.after(50,mover1)


def mover5():
    """ 
    funcion que realiza el movimiento de el primer enemigo
    """

    global posxmalo,posymalo,malo,ventana1,canvas1
    canvas1.delete(malo)
    malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    posxmalo=posxmalo+4
    #print(posxmalo, "posymalo",posymalo)
    if(posxmalo>742):
        canvas1.delete(malo)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        posxmalo=posxmalo-800
    if(posxmalo==320 and posymalo==100):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==540 and posymalo==220):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==300 and posymalo==340):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    if(posxmalo>670 and posymalo==460):
        canvas1.delete(malo)
        posxmalo=100
        posymalo=100
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    ventana1.after(15,mover5)

def mover3():
    """ 
    funcion que realiza el movimiento de el primer enemigo
    """

    global posxmalo,posymalo,malo,ventana1,canvas1
    canvas1.delete(malo)
    malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    posxmalo=posxmalo+4
    #print(posxmalo, "posymalo",posymalo)
    if(posxmalo>742):
        canvas1.delete(malo)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        posxmalo=posxmalo-800
    if(posxmalo==320 and posymalo==100):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==540 and posymalo==220):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
    if(posxmalo==300 and posymalo==340):
        canvas1.delete(malo)
        posymalo=posymalo+120
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    if(posxmalo>670 and posymalo==460):
        canvas1.delete(malo)
        posxmalo=100
        posymalo=100
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        
    ventana1.after(25,mover3)


def mover2():
    """
    funcion que realiza el movimiento del segundo enemigo 
    """
    global posxmalo2,posymalo2,malo2,ventana1,canvas1
    canvas1.delete(malo2)
    malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    posxmalo2=posxmalo2-4
    
    if(posxmalo2<-60):
        canvas1.delete(malo2)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        posxmalo2=posxmalo2+800
    if(posxmalo2==400 and posymalo2==100):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==180 and posymalo2==220):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==460 and posymalo2==340):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
    if(posxmalo2<10 and posymalo2==460):
        canvas1.delete(malo2)
        
        posxmalo2=700
        posymalo2=100
        malo2=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1)
        
    ventana1.after(50,mover2)

def mover4():
    """
    funcion que realiza el movimiento del segundo enemigo 
    """
    global posxmalo2,posymalo2,malo2,ventana1,canvas1
    canvas1.delete(malo2)
    malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    posxmalo2=posxmalo2-4
    
    if(posxmalo2<-60):
        canvas1.delete(malo2)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        posxmalo2=posxmalo2+800
    if(posxmalo2==400 and posymalo2==100):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==180 and posymalo2==220):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==460 and posymalo2==340):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
    if(posxmalo2<10 and posymalo2==460):
        canvas1.delete(malo2)
        
        posxmalo2=700
        posymalo2=100
        malo2=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1)
        
    ventana1.after(25,mover4)


def mover6():
    """
    funcion que realiza el movimiento del segundo enemigo 
    """
    global posxmalo2,posymalo2,malo2,ventana1,canvas1
    canvas1.delete(malo2)
    malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    posxmalo2=posxmalo2-4
    
    if(posxmalo2<-60):
        canvas1.delete(malo2)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        posxmalo2=posxmalo2+800
    if(posxmalo2==400 and posymalo2==100):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==180 and posymalo2==220):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
    if(posxmalo2==460 and posymalo2==340):
        canvas1.delete(malo2)
        posymalo2=posymalo2+120
        malo=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
    if(posxmalo2<10 and posymalo2==460):
        canvas1.delete(malo2)
        
        posxmalo2=700
        posymalo2=100
        malo2=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1)
        
    ventana1.after(15,mover6)
    
    
            


                        

###### en esta funcion se definen los distintos ventanas y canvas para los niveles


def dificultad(event):
    global canvas1,pj,ventana1,enemigo1,pj2,malo
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
        pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
        ventana1.after(10,mover1)
        ventana1.after(10,mover2)
        

       
            
    



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
        pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
        ventana1.after(10,mover3)
        ventana1.after(10,mover4)





    elif(tecla=="'e"):      
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
        pj2=canvas1.create_image(posxm,posym,anchor=NW,image=mario)
        malo=canvas1.create_image(posxmalo,posymalo,anchor=NW,image=malo1d)
        malo2=canvas1.create_image(posxmalo2,posymalo2,anchor=NW,image=malo1)
        
        ventana1.after(10,mover5)
        ventana1.after(10,mover6)
        
        
        
        
      
        
        ventana1.mainloop()

        

       
######################################################
def Call(): # Definimos la funcion
    global ventanajuego
    ventanajuego= Toplevel()
    ventanajuego.geometry("900x506")
    canvas= Canvas(ventanajuego,width=894,height=506)
    canvas.create_image(0,0,anchor=NW,image=niveles)
    btnivel1= Button(ventanajuego,text="FACIL Presionar Q",font=("Agenci FB",17),bg="#33A6DF").place(x=70,y=70)
    btnivel2= Button(ventanajuego,text="NORMAL  Presionar W",font=("Agenci FB",17),bg="#0E81BA").place(x=70,y=210)
    btnivel3= Button(ventanajuego,text="MEDIO  Presionar E",font=("Agenci FB",17),bg="#954CAB").place(x=70,y=360)
    btnivel4= Button(ventanajuego,text="FRIKASO Presionar R",font=("Agenci FB",17),bg="#F5F076").place(x=620,y=170)
    btnivel5= Button(ventanajuego,text="Legendario Presionar T",font=("Agenci FB",17),bg="#E21709").place(x=620,y=300)

    #cajondetexto=StringVar()
    #variable1=Entry(ventanajuego,textvariable=cajondetexto).place(x=200,y=300)
    #nombre=str(variable1.get())
    #nombreusuario1=Label(canvas,text=nombre,font=("Agenci FB",13)).place(x=210,y=310)

    canvas.pack()
    canvas.focus_set()
    canvas.bind("<Key>", dificultad)
    ventanajuego.mainloop()


def ventanainstrucciones():
    global ventanaminstru,canvas2
    ventanainstru= Toplevel()
    ventanainstru.geometry("800x500")
    fondoinstru=Label(ventanainstru,image=instrucciones).place(x=0,y=0)
    Btnback1= Button(ventanainstru,text="VOLVER",font=("Agenci FB",13),command= ventanainstru.destroy).place(x=0,y=0)
    
#########################################    #########
def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño : Anderson laverde \n y codigo : Anderson laverde Gracia \n Contacto :  \n Pagina de Facebook : http://goo.gl/IwPKtl   \n Codigo Fuente : https://github.com/andirsun/mario.git ")
########################################    
boton= Button(ventanamenu,text="JUGAR",font=("Agenci FB",13),command= Call,bg="#0080FF",cursor="crosshair",relief="groove",activebackground="#F50743").place(x=440,y=340)
boton2= Button(ventanamenu,text="CARGAR",font=("Agenci FB",13),bg="#FF3333",cursor="dotbox",relief="groove",activebackground="#F50743").place(x=435,y=390)
boton3= Button(ventanamenu,text="CREDITOS",font=("Agenci FB",13),command=creditos,bg="#0080FF",cursor="fleur",relief="groove",activebackground="#F50743").place(x=430,y=440)
boton4= Button(ventanamenu,text="INSTRUCCIONES",font=("Agenci FB",13),command=ventanainstrucciones,bg="#FF3333",cursor="pirate",relief="groove",activebackground="#F50743").place(x=410,y=480)
boton5= Button(ventanamenu,text="SALIR",font=("Agenci FB",13),command=ventanamenu.destroy,bg="#FF3333",cursor="pirate",relief="groove",activebackground="#F50743").place(x=448,y=520)
#########################################

ventanamenu.mainloop() 
