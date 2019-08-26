### INICIALIZAR VPYTHON
from vpython import *


### AJUSTAR ELEMENTOS DE LA SIMULACION
scale=50.0
scene.title = "Movimiento 1D"
scene.background=color.white


x01=5.0
x02=-10.0
bolita1=sphere(pos=(x01,0,0),radius=0.5,color=color.red)
bolita2=sphere(pos=(x02,0,0),radius=0.5,color=color.blue)
superficie = box(pos=(0,-(bolita1.radius+0.1),0),size=(2*scale,0.3,0.1),color = color.green)

 
##### CONDICIONES INICIALES
### ----------------------------------------------------------------------------------------
 
bolita1.pos=vector(x01,0,0)
bolita1.v=vector(15.0,0,0)
bolita1.a=vector(4.0,0,0)

bolita2.pos=vector(x02,0,0)
bolita2.v=vector(0.0,0,0)
bolita2.a=vector(30.0,0,0)
 
t=0 #TIEMPO INICIAL
deltat = 0.1 #PASO TEMPORAL
 
### ECUACIONES DE LA CINEMATICA MOVIMIENTO UNIFORMEMENTE ACAELERADO

pos01=bolita1.pos.x #POSICION INICIAL
vel01=bolita1.v.x #VELOCIDAD INICIAL
a01=bolita1.a.x #ACELERACION
pos02=bolita2.pos.x #POSICION INICIAL
vel02=bolita2.v.x #VELOCIDAD INICIAL
a02=bolita2.a.x #ACELERACION
print ("t=",t, "x=",bolita1.pos.x, "vx=",bolita1.v.x, "ax=",bolita1.a.x)
print ("t=",t, "x=",bolita2.pos.x, "vx=",bolita2.v.x, "ax=",bolita2.a.x)
### ##### CICLO DE ANIMACION
### IMPRIMIR EN PANTALLA TIEMPO, POSICION, VELOCIDAD, ACELERACION,....

while t<=3.0:#mibolita.pos.x>=-scale and mibolita.pos.x<=scale:
    rate(100)
    t=t+deltat
    bolita1.pos.x=pos01+vel01*t+0.5*a01*t**2
    bolita1.v.x=vel01+a01*t
    bolita2.pos.x=pos02+vel02*t+0.5*a02*t**2
    bolita2.v.x=vel02+a02*t
    print ("t=",t, "x=",bolita1.pos.x, "vx=",bolita1.v.x, "ax=",bolita1.a.x)
    print ("t=",t, "x=",bolita2.pos.x, "vx=",bolita2.v.x, "ax=",bolita2.a.x)
   
    



 
    
