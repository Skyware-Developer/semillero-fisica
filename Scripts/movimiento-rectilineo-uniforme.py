from vpython import scene, sphere, vector, color, rate

scene.autoscale = False

scale = 10.0

mibolita = sphere(pos=vector(-9.0, 0, 0), radius=0.5, color=color.red)

dt = 0.1

v = 0.5

while True:
    rate(70)
    mibolita.pos.x = mibolita.pos.x + v*dt
