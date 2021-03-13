import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate

def f(t,x,u):
    dx = np.empty(1)
    dx = -u*x
    return np.array(dx)


def DDMRkinematic(q,t,dphi):
    #%Parameters
    R = 1
    L = 1
    #q1,q2,q3 = q 
    dq = np.empty(3)
    dq[0] =R*math.cos(q[2])*(dphi[0]+dphi[1])/2
    dq[1] = R*math.sin(q[2])*(dphi[0]+dphi[1])/2
    dq[2] =  R*(dphi[0]-dphi[1])/(2*L)
    return dq

def erroCart2pol(qk,refXY):
    erroXY = refXY - qk[0:2]
    refTheta = math.atan2(erroXY[1],erroXY[0])
    erroTheta = refTheta - qk[2]
    mod = math.sqrt(refXY[0]**2+refXY[1]**2)
    ang = erroTheta
    return mod,ang



q0 = np.array([2.4,10.8,0])
Ts = 0.01
velMax = 3 #rad/s
qk = q0
ref = np.array([10,10])#np.array([2.8,10.8])
q = qk 
positionGain = 0.01*np.array([1,1])
angleGain = 1*np.array([1,-1])

(mod,ang) = erroCart2pol(qk,ref)

control = mod*positionGain + ang*angleGain

t = np.linspace(0,10,101)
sol = integrate.odeint(DDMRkinematic,q0,t,args=(control,))

print(sol[:,0])
q1 = sol[:,0]
q2 = sol[:,1]
q3 = sol[:,2]

plt.plot(q1,q2)
plt.xlabel('x(t)')
plt.ylabel('y(t)') 
plt.grid()
plt.show()
#plt.plot(ref)
#plt.show()