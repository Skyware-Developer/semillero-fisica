from vpython import sphere, box, scene, vector, rate, color

scene.range = 20
ball = sphere(radius= 1, pos=vector(0, 0, 0), color=color.blue)

leftBorder = box(pos=vector(-30, 0, 0), size=vector(1, 20, 1), color=color.red)
rightBorder = box(pos=vector(30, 0, 0), size=vector(1, 20, 1), color=color.red)

vx = 10
ball.velocity = vector(vx, 0, 0)

dt = 0.01

t = 0

while t < 20:    
    rate(100)
    ball.pos = ball.pos + (ball.velocity * dt)
    t = t+dt    
    if ball.pos.x - ball.radius > rightBorder.pos.x - 2:
        ball.velocity = -ball.velocity
    if ball.pos.x + ball.radius < leftBorder.pos.x + 2:
        ball.velocity = -ball.velocity


