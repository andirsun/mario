
import tkinter


v = tkinter.Tk()

posx = 0
posy = 0
limite = False
presionado = [0,0,0,0]

def saltar():
    """
    Procedimiento que realiza el salto
    """
    global v,canvas,cuadrado,posx,posy,limite
    if(not limite):
        posy = posy - 10
    else:
        posy = posy + 10
    if(posy > -200 and not limite):
        canvas.delete(cuadrado)
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")
        v.after(10,saltar)
    else:
        limite = True
        canvas.delete(cuadrado)
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")
        if(posy != 0):
            v.after(10,saltar)

def saltar2():
    """
    Procedimiento que realiza el salto en parabola
    """
    global v,canvas,cuadrado,posx,posy,limite
    if(not limite):
        posy = posy - 10
    else:
        posy = posy + 10
    posx = posx + 1
    if(posy > -200 and not limite):
        canvas.delete(cuadrado)
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")
        v.after(10,saltar2)
    else:
        limite = True
        canvas.delete(cuadrado)
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")
        if(posy != 0):
            v.after(10,saltar2)

        
def pressed(event):
    global canvas,cuadrado,posx,posy,limite
    tecla = repr(event.char)
    if(tecla == "'w'"):
        presionado[0] = True
        if(presionado[3] == True):
            limite = False
            saltar2()
        else:
            limite = False
            saltar()
    elif(tecla == "'a'"):
        presionado[1] = True
        canvas.delete(cuadrado)
        posx = posx - 1
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")
    elif(tecla == "'s'"):
        presionado[2] = True
    elif(tecla == "'d'"):
        presionado[3] = True
        canvas.delete(cuadrado)
        posx = posx + 1
        cuadrado = canvas.create_polygon(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,fill="purple")

def released(event):
    global canvas,cuadrado,posx,posy,limite
    tecla = repr(event.char)
    if(tecla == "'w'"):
        presionado[0] = False
    elif(tecla == "'a'"):
        presionado[1] = False
    elif(tecla == "'s'"):
        presionado[2] = False
    elif(tecla == "'d'"):
        presionado[3] = False

canvas = tkinter.Canvas(v,width=500,height=500)
for char in ["w","a","s", "d"]:
    canvas.bind("<KeyPress-%s>" % char, pressed)
    canvas.bind("<KeyRelease-%s>" % char, released)
canvas.focus_set()
canvas.pack()

imagen = tkinter.PhotoImage(file='mario.gif')
canvas.create_image(200,200, image=imagen)
cuadrado = canvas.create_polygon(200,400,200,450,250,450,250,400,fill="purple")


v.mainloop()
