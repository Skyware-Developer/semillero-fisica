from vpython import sphere, box, scene, vector, rate, color, curve

scene.range = 20
ball = sphere(radius=1, pos=vector(0, 0, 0), color=color.green)

leftBorder = box(pos=vector(-20, 0, 0), size=vector(1, 40, 40), color=color.red)
rightBorder = box(pos=vector(20, 0, 0), size=vector(1, 40, 40), color=color.red)
topBorder = box(pos=vector(0, 20, 0), size=vector(40, 1, 40), color=color.blue)
bottomBorder = box(pos=vector(0, -20, 0), size=vector(40, 1, 40), color=color.blue)
frontBorder = box(pos=vector(0, 0, 20), size=vector(40, 40, 1), color=color.red, opacity = 0.1)
bgBorder = box(pos=vector(0, 0, -20), size=vector(40, 40, 1), color=color.gray(0.8))

ball.trail = curve(color=ball.color)

vx = 12
vy = 10
vz = 8
ball.velocity = vector(vx, vy, vz)

dt = 0.01

t = 0

while t < 20:
    rate(100)
    ball.pos = ball.pos + (ball.velocity * dt)
    ball.trail.append(pos=ball.pos)
    t = t+dt
    if ball.pos.x + ball.radius > rightBorder.pos.x:
        ball.velocity.x = ball.velocity.x * (-1)
    if ball.pos.x - ball.radius < leftBorder.pos.x:
        ball.velocity.x = ball.velocity.x * (-1)
    if ball.pos.y + ball.radius > topBorder.pos.y:
        ball.velocity.y = ball.velocity.y * (-1)
    if ball.pos.y - ball.radius < bottomBorder.pos.y:
        ball.velocity.y = ball.velocity.y * (-1)
    if ball.pos.z + ball.radius > frontBorder.pos.z:
        ball.velocity.z = ball.velocity.z * (-1)
    if ball.pos.z - ball.radius < bgBorder.pos.z:
        ball.velocity.z = ball.velocity.z * (-1)