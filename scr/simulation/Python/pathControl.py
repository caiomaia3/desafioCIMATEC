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
        return control
        
    def saturateControl(control,limit):
        saturatedControl= numpy.array([])
        for signal in control:
            isSaturated = (abs(signal)-limit)>0
            if isSaturated:
                signal = numpy.sign(signal)*limit
            saturatedControl = numpy.append(saturatedControl,signal)
        return saturatedControl 

 