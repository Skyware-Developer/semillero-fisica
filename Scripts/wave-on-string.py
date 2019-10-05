from numpy import *
from  matplotlib.pyplot import *

# Variables
N = 201 # Number of mass points
nT = 1200 # Number of time points
mi = 0.02 # mass in kg
m = [mi]*N # mass array
m[-1] = 100 # Large last mass reflective edges
m[0] = 100 # Large first mass  reflective edges
ki = 10.#spring 
k = [ki]*N
k[-1] = 0
dx = 0.2
kappa = ki*dx
my = mi/dx
c = sqrt(kappa/my) # velocity 

dt = 0.04

#  3 vectors
x = arange( N )*dx # x points
t = arange( N )*dt # t points
y = zeros( [N, nT ] )# 2D array


# Loop over initial condition
for i in range(N-1):
    ci_i = sin(7.*pi*i/(N-1)) # Initial condition dependent on mass point
    if np.sign(ci_i*y[i-1,0])<0:
        break
    else:
        y[i,0] = ci_i


# Iterating over time and position to find next position of wave
for j in range(nT-1):

    for i in range(N-1):
        y[i,j+1] = 2*y[i,j] - y[i,j-1] + (dt**2/m[i])*(k[i-1]*y[i+1,j] -2*k[i-1]*y[i,j] + k[i]*y[i-1,j] )

    #check values of edges
    print (y[:2,j+1],y[-2:,j+1])

    # Creates an animation    
    cla()
    title('Ondas en una cuerda')
    ylabel("Amplitud")
    xlabel("x")    
    ylim(-10,10)
    plot(x,y[:,j-2])    
    pause(0.001)
    
    
close()
