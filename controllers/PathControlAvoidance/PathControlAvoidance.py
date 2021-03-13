"""PathControlAvoidance controller."""
from controller import Motor,GPS,InertialUnit,DistanceSensor,Robot
from pathControl import ProportionalControl as pControl
from pathControl import ObstacleAvoidance as oav
import numpy as np
import csv

TIME_STEP = 16
MAX_VEL = 12

#Index
xyz_Zposition = 2
xyz_Xposition = 0
zRotation = 2

#Load trajectory
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
trajectoryList.reverse() #Make a stack
del(newList)


#Robot instance
robot = Robot()

#Device instances
#Actuators
#Whell motors
leftMotor = robot.getDevice('left wheel')
rightMotor = robot.getDevice('right wheel')
##Device configuration
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0*MAX_VEL)
rightMotor.setVelocity(0*MAX_VEL)

#Sensors
#Distante sensors
so0 = DistanceSensor('so0')
so0.enable(TIME_STEP)
so2 = DistanceSensor('so2')
so2.enable(TIME_STEP)
so5 = DistanceSensor('so5')
so5.enable(TIME_STEP)
so7 = DistanceSensor('so7')
so7.enable(TIME_STEP)


gpsSensor = GPS('gps')
gpsSensor.enable(TIME_STEP)
inercialSensor = InertialUnit('inertialUnit')
inercialSensor.enable(TIME_STEP)


#The Control Loop
#Tuning of Controller
atReference =False
angleGain = 1000
positionGain = 10
referencePosition = trajectoryList.pop()
robotDirection = oav.makeRobotDirectionVector()

interruptionCounter = 0
radius = 400
while robot.step(TIME_STEP) != -1:
    # #Sensoring
    xyz = gpsSensor.getValues()
    rotation =inercialSensor.getRollPitchYaw()

    sensorList = [so0,so2,so5,so7]
    numberList = [0,2,5,7]
    avoidanteRotation = oav.calculateAvoidanceRotation(robotDirection,sensorList,numberList,radius)

    #Data manipulation
    states = np.array([xyz[xyz_Zposition],xyz[xyz_Xposition],rotation[zRotation]])
   
    # #Setting reference
    endOfTrajectory = len(trajectoryList)<=0
    if not endOfTrajectory:
        if atReference:
            referencePosition = trajectoryList.pop()
        atReference = all( abs(states[0:2]-referencePosition)< 0.15)#10
    else:
        angleGain = 0
        positionGain = 0

    #Calculating Control Effort
    if abs(avoidanteRotation) >0:
        aux = avoidanteRotation
        interruptionCounter = 10
        
    if interruptionCounter > 0:
        interruptionCounter = interruptionCounter -1
        magnitude,direction = pControl.calculatePolarError(states,referencePosition)
        control = pControl.calculateKinematicControl(magnitude,100*aux/1000,10*angleGain,angleGain)
    else:
        magnitude,direction = pControl.calculatePolarError(states,referencePosition)
        control = pControl.calculateKinematicControl(magnitude,direction,positionGain,angleGain)
    maxControl = np.max(abs(control))
    if (not maxControl == 0):
        control = MAX_VEL*control/maxControl
    control = pControl.saturateControl(control,MAX_VEL)

    #Set Reference Wheel Velocity
    if endOfTrajectory:
        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)
    else:
        leftMotor.setVelocity(control[1])
        rightMotor.setVelocity(control[0])
