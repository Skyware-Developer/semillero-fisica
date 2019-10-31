from numpy import *
from  matplotlib.pyplot import *

A = 5 # Amplitud de la onda

# Variables
N = 201 # Número de puntos de masa
nT = 1200
mi = 0.02
m = [mi]*N # Array de puntos de masa
m[-1] = 100 
m[0] = 100 
ki = 10.
k = [ki]*N
k[-1] = 0
dx = 0.2
kappa = ki*dx
my = mi/dx
c = sqrt(kappa/my) # Rapidez

dt = 0.04
#  Vectores 
x = arange( N )*dx # Puntos en X
t = arange( N )*dt # Puntos en t
y = zeros( [N, nT ] )# Array 2D auxiliar


# Ciclo inicializador
for i in range(N-1):
    ci_i = (A * 0.1) * sin(7.*pi*i/(N-1)) # Condiciones iniciales

    if np.sign(ci_i*y[i-1,0])<0:
        break
    else:
        y[i,0] = ci_i


# Iteración que busca la siguiente posición de la onda en el espacio-tiempo
for j in range(nT-1):

    for i in range(N-1):
        y[i,j+1] = 2 * y[i,j] - y[i,j-1] + (dt**2/m[i]) * (k[i-1] * y[i+1,j] - 2 * k[i-1] * y[i,j] + k[i] * y[i-1,j]) # Fórmula de la onda

    # Creación de la animación
    cla()
    title('Ondas en una cuerda')
    ylabel("Amplitud")
    xlabel("x")
    ylim(-A-2,A+2)
    plot(x,y[:,j-2])  
    pause(0.001)
    
close()
