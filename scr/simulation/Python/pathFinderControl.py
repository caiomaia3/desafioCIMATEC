import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import scipy.integrate as integrate
import csv
from pathControl import ProportionalControl as pControl

def calculatePolarError(states,referencePosition):
    errorPosition = referencePosition - states[0:2]
    referenceAngle = math.atan2(errorPosition[1],errorPosition[0])
    errorAngle = referenceAngle - states[2]
    magnitude = math.sqrt(errorPosition[0]**2+errorPosition[1]**2)
    direction = errorAngle 
    return magnitude,direction 

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
    mod = math.sqrt(erroXY[0]**2+erroXY[1]**2)
    ang = erroTheta
    return mod,ang

def saturate(control,limit):
    saturatedControl= np.array([])
    for signal in control:
        isSaturated = (abs(signal)-limit)>0
        if isSaturated:
            signal = np.sign(signal)*limit
        saturatedControl = np.append(saturatedControl,signal)
    return saturatedControl 

#carregar tragetória
trajectoryList = []
with open('trajetoria.csv',newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=',')
    for row in spamreader:
       trajectoryList.append(row) 

newList = []
for l in trajectoryList:
    aux = [float(s) for s in l]
    newList.append(1*np.array(aux))

trajectoryList = newList
del(newList)
refPlot = trajectoryList
trajectoryList.reverse()#Make a stack
q0 = np.append(trajectoryList.pop(),np.array([0]))
Ts = 0.01
velMax = 3 #rad/s
qk = q0
ref = trajectoryList.pop()
q = qk 
#Control configuration
positionGain = 1*np.array([1,1])
angleGain = 100*np.array([1,-1])

(mod,ang) = erroCart2pol(qk,ref)
control = mod*positionGain + ang*angleGain
control = saturate(control,velMax)

t = np.linspace(0,Ts,2)
qPlot = np.array([q0])  
simulPlot = np.array([q0])  
refPlot = np.array([ref])
atReference =False 
#while len(trajectoryList)>0:
i=0
print(len(trajectoryList))
while (len(trajectoryList)>0):
# for i in range(4):
    while not atReference:
        (mod,ang) = pControl.calculatePolarError(qk,ref)
        control = pControl.calculateKinematicControl(mod,ang,1,100)
        control = pControl.saturateControl(control,velMax)
        sol = integrate.odeint(DDMRkinematic,qk,t,args=(control,))
        simulPlot = np.append(simulPlot,np.array([sol[1]]),axis=0)
        qk = sol[1]
        atReference = all( abs(qk[0:2]-ref)< 0.05 )

    qPlot = np.append(qPlot,np.array([qk]),axis=0)
    ref = trajectoryList.pop()
    refPlot = np.append(refPlot,np.array([ref]),axis=0)
    atReference = False
    print(str(len(trajectoryList)) + '---' +str(atReference)+'---'+str(control))

plt.plot(simulPlot[:,0],simulPlot[:,1])
plt.scatter(qPlot[:,0],qPlot[:,1])
plt.scatter(refPlot[:,0],refPlot[:,1])
#plt.plot(simulGraph[1::,0],t)

plt.xlabel('x(t)')
plt.ylabel('y(t)') 
plt.grid()
plt.show()
#plt.plot(ref)
#plt.show()