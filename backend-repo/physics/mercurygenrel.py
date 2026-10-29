# Noah Kops, 10/28/26
import numpy as np
import astropy.constants as const
import astropy.units as u
#import scipy as sp
import matplotlib.pyplot as plt
import math
import time



G = const.G.value
M = const.M_sun.value
c = const.c.value
#dt=100
T=87.969*24*3600+24*3600 #single orbital period with some buffer
r_0 = 46001200*1000 # periapsis
vr_0 = 0
theta_0 = 0
v_theta_0 = 58.98*1000/r_0
state=[r_0,vr_0,theta_0,v_theta_0]
range03 = [0,1,2,3]

x_data = []
y_data = []

def differentiate(state): # state= r,vr, theta, v_theta
   r, vr, theta, v_theta = state
   l = r*r*v_theta
   ar = -G*M/(r*r) + l*l/(r*r*r) - 3*G*M*l*l/(c*c*r*r*r*r)
   # l = r^2 omega, dl/dt=0, 2r vr omega = - r^2 alpha, alpha= -2vr omega / r
   a_theta = -2*vr*v_theta/r 
   return [vr,ar,v_theta,a_theta]
def rungeKutta(slopes,dt):
   return [slopes[0][i]*dt/6
          + 2*slopes[1][i]*dt/6
          + 2*slopes[2][i]*dt/6
          + slopes[3][i]*dt/6
          for i in range03]
def runSim(dt):
   t=0
   midpoint1 = [0,0,0,0]
   midpoint2 = [0,0,0,0]
   endpoint1 = [0,0,0,0]
   global state
   while t<T:
      t=t+dt
      k1 = differentiate(state)
      
      for i in range03:
         midpoint1[i] = state[i] + k1[i]*dt/2
         
      k2 = differentiate(midpoint1)
      
      for i in range03:
         midpoint2[i] = state[i] + k2[i]*dt/2
         
      k3 = differentiate(midpoint2)
      
      for i in range03:
         endpoint1[i] = state[i] + k3[i]*dt
         
      k4 = differentiate(endpoint1)
      
      
      for i in range03:
         midpoint1[i] = state[i] + k1[i]*dt/2
      
      runge = rungeKutta([k1,k2,k3,k4],dt)
      
      oldVr = state[1]
      for i in range03:
         state[i] = state[i] + runge[i]
      if oldVr*state[1]<=0: #turn around, periapsis apoapsis
         print((state[2]%(2*math.pi))*u.radian.to(u.arcsec)) # angle 
         print(state)
         print(f"difference {(state[0]-r_0)} meters")
      
     
      

# #       
# 
