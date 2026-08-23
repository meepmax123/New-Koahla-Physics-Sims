import numpy as np
import matplotlib.pyplot as plt
import math

# We will define our physical constants here.
G = 6.674e-11
M = 1.989e30
c = 2.99e8
l=0
range03=np.array([0,1,2,3])

def setL(r, v_theta):
  l=r**2*v_theta


def differentiate(state):
  r, v_r, theta, v_theta=state
  l = r**2*v_theta
  #radial acceleration = -dV/dr = -GM/r^2 + l^2/r^3 - 3GMl^2/c^2r^4
  dvr_dt = -G*M/(r*r) + l*l/(r*r*r) - 3*G*M*l*l/(c*c*r*r*r*r)
  dr_dt = v_r #radial velocity
  dtheta_dt = v_theta #angular velocity
  #angular acceleration = -2 vr vtheta / r
  dvtheta_dt = -2*v_r*v_theta/r
  return [dr_dt, dvr_dt, dtheta_dt,dvtheta_dt]
def rungeKutta(slopes,dt):
  # slopes is a list of 4 lists: [k1, k2, k3, k4]
  # Each k_i is a list of 4 elements (dr_dt, dvr_dt, dtheta_dt, dvtheta_dt)
  # The formula is (k1 + 2*k2 + 2*k3 + k4) * dt / 6
  return [slopes[0][i]*dt/6
          + 2*slopes[1][i]*dt/6
          + 2*slopes[2][i]*dt/6
          + slopes[3][i]*dt/6
          for i in range03]
  # sum_terms = add(slopes[0], scale(slopes[1], 2))
  # sum_terms = add(sum_terms, scale(slopes[2], 2))
  # sum_terms = add(sum_terms, slopes[3])
  # return scale(sum_terms, dt / 6)


def run_mercurygenrel_simulation(data):
    

    dt = 100 # Adjusted for performance; feel free to refine
    r_perihelion = 4.6e10
    v_perihelion = 5.9e4
    pi = math.pi
    
    # Calculate initial v_theta using v = r * v_theta
    state = [r_perihelion, 0, 0, v_perihelion / r_perihelion]
    
    perihelionAngles = [0.0]
    print(state)
    # Set total time for ~2 orbits (2 * 88 days)
    t_max = 2 * 88 * 24 * 3600
    time = np.arange(0, t_max, dt)
    oldv_r = 0.0
    setL(state[0],state[3])
    
    midpoint1 = [0,0,0,0]
    midpoint2 = [0,0,0,0]
    endpoint1 = [0,0,0,0]
    
    r,vr, th, vt = state
    for t in time:
      # oldState = state
      # states = [0,0,0,0,0]
    
      # for k in range(1,5):
      #   derivative = differentiate(state)
      #   state = [state[i]+derivative[i]*dt/4 for i in [0,1,2,3]]
      #   states[k] = state`lo0-;p./'
      # state = rungeKutta(states, dt)
      k1 = differentiate(state)
      # midpoint1 = [state[i]+k1[i]*dt/2 for i in range03]
      midpoint1[0]=r+k1[0]*dt/2
      midpoint1[1]=vr+k1[1]*dt/2
      midpoint1[2]=th+k1[2]*dt/2
      midpoint1[3]=vt+k1[3]*dt/2
    
      #add(state,scale(k1,dt/2))
      k2 = differentiate(midpoint1)
      # midpoint2 = [state[i]+k2[i]*dt/2 for i in range03]
      midpoint2[0]=r+k1[0]*dt/2
      midpoint2[1]=vr+k1[1]*dt/2
      midpoint2[2]=th+k1[2]*dt/2
      midpoint2[3]=vt+k1[3]*dt/2
    
      #add(state,scale(k2,dt/2))
      k3 = differentiate(midpoint2)
      # endpoint1 = [state[i]+k3[i]*dt for i in range03]
      endpoint1[0]=r+k3[0]*dt
      endpoint1[1]=vr+k3[1]*dt
      endpoint1[2]=th+k3[2]*dt
      endpoint1[3]=vt+k3[3]*dt
    
      #add(state,scale(k3,dt))
      k4 = differentiate(endpoint1)
      runge = rungeKutta([k1,k2,k3,k4],dt)
      r=r+runge[0]
      vr=vr+runge[1]
      th=th+runge[2]
      vt=vt+runge[3]
      #state = [state[i] + runge[i] for i in range03]
      #add(state,rungeKutta([k1,k2,k3,k4],dt))
      th=th%(2*pi)
      if oldv_r*vr<=0 and abs(th-perihelionAngles[len(perihelionAngles)-1])<=10.0*pi/180:
        perihelionAngles.append(th)
      oldv_r=vr
      state=r,vr,th,vt
    
    
    for i in range(len(perihelionAngles)-1):
      #print(180/pi*perihelionAngles[i])
    #print(len(perihelionAngles))
    #print(state)

    # return 180/pi*perihelionAngles[1]
    return {
        "result": (180/pi*perihelionAngles[1])
    }
