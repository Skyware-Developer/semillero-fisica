from __future__ import division
#from vpython import *
from vpython import sphere, box, scene, vector, rate, color



scene.range=10
ball=sphere(radius=0.3,pos=vector(0,4,0),color=color.blue)

ground=box(pos=vector(0,-4,0),size=vector(4,0.1,0.1))
vy=0.0
ay=-9.8
vscale=0.8
ball.velocity=vector(0,vy,0)

ball.acceleration=vector(0,ay,0)
dt=0.01

t=0

while ball.pos.y-ball.radius>ground.pos.y:
    rate(100)
    ball.velocity=ball.velocity+ball.acceleration*dt    
    ball.pos=ball.pos+(ball.velocity)*dt
    t=t+dt
    
