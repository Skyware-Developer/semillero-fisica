from numpy import *
from matplotlib.pyplot import *

#Crear una funcion con la derivada parcial resuelta y en cada punto que haga el cálculo de la fricción
#Entonces en cada punto muestre los datos evaluados.

# Variables
N = 1501 # Number of mass points
nT = 1000 # Number of time points
mi = 0.02 # mass in kg
m = [mi]*N # mass array
#m[-1] = 100 # Large last mass reflective edges
#m[0] = 100 # Large first mass  reflective edges
ki = 10.# spring 
k = [ki]*N
k[-1] = 0
dx = 0.2
kappa = ki*dx
my = mi/dx
c = sqrt(kappa/my) # velocity 
dt = 0.04
r = c * dt / dx
print('R')
print(r)
s = 0.1
x0 = 150


#  3 vectors
x = arange( N )*dx # x points
t = arange( N )*dt # t points
y = zeros( [N, nT ] )# 2D array


#set initial pulse shape
def init_fn(x):
    val = np.exp(-(x**2)/0.25)
    if val<.001:
        return 0.0
    else:
        return val


# Loop over initial condition
#for i in range(N-1):
    #ci_i = 0.5 * sin(7.*pi*i/(N-1)) # Initial condition dependent on mass point

    #ci_i = exp(-s*((i*dx)-x0)**2)
    #y[i,0] = ci_i
    #if np.sign(ci_i*y[i-1,0]) < 0:
    #    break
    #else:
    #    y[i,0] = ci_i

for a in range(0,nx):
    y[a,0]=init_fn(a*dx)
    y[a,1]=y[a,0]

# Iterating over time and position to find next position of wave
for j in range(nT-1):
    y[0,j]=0
    y[N-1,j]=0
    for i in range(1,N-1):
        #y[i,j+1] = 2*y[i,j] - y[i,j-1] + (dt**2/m[i])*(k[i-1]*y[i+1,j] -2*k[i-1]*y[i,j] + k[i]*y[i-1,j] )
        y[i,j+1] = (2 * (1-((r)**2)) * y[i,j]) - (y[i,j-1]) + ((r**2) * (y[i+1,j] + y[i-1,j]))
        
    #check values of edges
    print (y[:2,j+1],y[-2:,j+1])
    
    # Creates an animation
    cla()
    title('Ondas en una cuerda')
    ylabel("Amplitud")
    xlabel("x")
    ylim(-20,20)
    plot(x,y[:,j-2])    
    pause(0.001)
    
    
close()
