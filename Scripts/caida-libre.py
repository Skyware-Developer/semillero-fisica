from __future__ import division
#from vpython import *
from vpython import sphere, box, scene, vector, rate, color

scene.range=25
ball=sphere(radius=0.3,pos=vector(0,4,0),color=color.blue)

ground=box(pos=vector(0,-4,0),size=vector(4,0.1,0.1))
vy = 0.0
vx = 1
ay=-9.8
vscale=0.8
ball.velocity=vector(vx,vy,0)

ball.acceleration=vector(0,ay,0)
dt=0.01

t=0

while t < 20:
    rate(100)
    if ball.pos.y - ball.radius <= ground.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y == 0:
        print(ball.velocity)
        print(ball.pos)
    ball.velocity=ball.velocity+ball.acceleration*dt    
    ball.pos=ball.pos+(ball.velocity)*dt
    #ball.trail.append(pos =)
    t=t+dt

#while ball.pos.y-ball.radius>ground.pos.y:
#    if ball.pos == vector(0,4,0):
#        vy = vy * (-1)
#    rate(100)
#    ball.velocity=ball.velocity+ball.acceleration*dt    
#    ball.pos=ball.pos+(ball.velocity)*dt
#    t=t+dt
