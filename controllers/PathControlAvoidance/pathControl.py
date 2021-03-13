import numpy
class ProportionalControl:
    def calculatePolarError(states,referencePosition):
        errorPosition = referencePosition - states[0:2]
        referenceAngle = numpy.arctan2(errorPosition[1],errorPosition[0])
        errorAngle = referenceAngle - states[2]
        magnitude = numpy.sqrt(errorPosition[0]**2+errorPosition[1]**2)
        direction = errorAngle 
        return magnitude,direction 

    def calculateKinematicControl(magnitude,direction,positionGain,angleGain):
        vectorialPositionGain = positionGain*numpy.array([1,1])
        vectorialAngleGain = angleGain*numpy.array([1,-1])
        control = magnitude*vectorialPositionGain + direction*vectorialAngleGain
        return control #right / left
        
    def saturateControl(control,limit):
        saturatedControl= numpy.array([])
        for signal in control:
            isSaturated = (abs(signal)-limit)>0
            if isSaturated:
                signal = numpy.sign(signal)*limit
            saturatedControl = numpy.append(saturatedControl,signal)
        return saturatedControl

    def rotateAngle(referenceAngle,actualAngle):
        if referenceAngle<0:
            rotatedAngle = numpy.pi - referenceAngle - ProportionalControl.correctDomain(actualAngle)
        else:
            rotatedAngle = referenceAngle - numpy.pi - ProportionalControl.correctDomain(actualAngle)
        return rotatedAngle

    def correctDomain(angle):
        return numpy.sign(angle)*(abs(angle)%numpy.pi)


class ObstacleAvoidance:
    def makePotentialVector(sensorNumber,distance):
        k = 1#numericalCorrectorGain
        zeroPotential = numpy.zeros(3)
        if distance ==0:
            return zeroPotential
        else:
            if sensorNumber == 0:
                angle = 90*numpy.pi/180
            elif sensorNumber == 1:
                return zeroPotential
            elif sensorNumber == 2:
                angle = 30*numpy.pi/180 #Angle in radians
            elif sensorNumber == 5:
                angle = -30*numpy.pi/180 #Angle in radians
            elif sensorNumber == 7:
                angle = -90*numpy.pi/180 #Angle in radians
            else:
                return zeroPotential
        
        length = k*(1/(distance**4))
        pontential = numpy.array([numpy.cos(angle),numpy.sin(angle),0])
        return pontential

    def makeRobotDirectionVector():
        return numpy.array([1,0,0])

    def calculateControlEffort(pontentialVector,robotDirection):
        rotation = numpy.cross(pontentialVector,robotDirection)
        return rotation[-1]

    def calculateAvoidanceRotation(robotDirection,sensorList,numberList,radius):
        rotation = 0
        for sensor,sensorNumber in zip(sensorList,numberList):
            if sensor.getValue()<radius:
                vref = ObstacleAvoidance.makePotentialVector(sensorNumber,sensor.getValue())
                rotation = rotation + ObstacleAvoidance.calculateControlEffort(vref,robotDirection)
        return rotation
