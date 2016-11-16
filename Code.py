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
megaman= PhotoImage(file="megaman.png")
malo1= PhotoImage(file="fantasma1.png")
malo2= PhotoImage(file="fantasma2.png")
malo3= PhotoImage(file="fantasma3.png")
malo4= PhotoImage(file="fantasma4.png")


###### prueba de variables para el salto
posy=-4

################## en esta funcion se definen los movimientos para el personaje principal y para los enemigos 
def teclado(event):
    global canvas1,pj
    tecla = repr(event.char)
    if(tecla == "'a'"):
        canvas1.move(pj,-3,0)
    elif(tecla=="'d'"):
        canvas1.move(pj,3,0)
    

    
                    
                
                

###### en esta funcion se definen los distintos ventanas y canvas para los niveles 
def dificultad(event):
    global canvas1,pj,ventana1
    tecla = repr(event.char)
    if(tecla=="'q'"):      
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
        pj=canvas1.create_image(200,415,anchor=NW,image=megaman)
        
        enemigo1=canvas1.create_image(20,50,anchor=NW,image=malo1)
        enemigo2=canvas1.create_image(30,60,anchor=NW,image=malo2)
        enemigo3=canvas1.create_image(40,70,anchor=NW,image=malo3)
        enemigo4=canvas1.create_image(50,80,anchor=NW,image=malo4)
        
        ventana1.mainloop()

        

        

         






    









######################################################
def Call(): # Definimos la funcion
    global ventanajuego
    ventanajuego= Toplevel()
    ventanajuego.geometry("900x506")
    canvas= Canvas(ventanajuego,width=894,height=506)
    canvas.create_image(0,0,anchor=NW,image=niveles)
    btnivel1= Button(ventanajuego,text="Si desea nivel 1 Presionar Q",font=("Agenci FB",13)).place(x=70,y=70)
    btnivel1= Button(ventanajuego,text="Si desea nivel 2 Presionar W",font=("Agenci FB",13)).place(x=70,y=70)
    btnivel1= Button(ventanajuego,text="Si desea nivel 1 Presionar E",font=("Agenci FB",13)).place(x=70,y=70)
    btnivel1= Button(ventanajuego,text="Si desea nivel 1 Presionar R",font=("Agenci FB",13)).place(x=70,y=70)
    btnivel1= Button(ventanajuego,text="Si desea nivel 1 Presionar T",font=("Agenci FB",13)).place(x=70,y=70)
    canvas.pack()
    canvas.focus_set()
    canvas.bind("<Key>", dificultad)
    ventanajuego.mainloop()
#########################################    #########
def creditos():
    messagebox.showinfo(title="CREDITOS",message="Diseño : Anderson laverde \n y codigo : Anderson laverde Gracia \n Contacto :  \n Pagina de Facebook : http://goo.gl/IwPKtl ")
########################################    
boton= Button(ventanamenu,text="JUGAR",font=("Agenci FB",13),command= Call,bg="#0080FF",cursor="crosshair",relief="groove",activebackground="#F50743").place(x=440,y=340)
boton2= Button(ventanamenu,text="CARGAR",font=("Agenci FB",13),bg="#FF3333",cursor="dotbox",relief="groove",activebackground="#F50743").place(x=435,y=390)
boton3= Button(ventanamenu,text="CREDITOS",font=("Agenci FB",13),command=creditos,bg="#0080FF",cursor="fleur",relief="groove",activebackground="#F50743").place(x=430,y=440)
boton4= Button(ventanamenu,text="SALIR",font=("Agenci FB",13),command=ventanamenu.destroy,bg="#FF3333",cursor="pirate",relief="groove",activebackground="#F50743").place(x=448,y=490)
#########################################


























ventanamenu.mainloop() 
