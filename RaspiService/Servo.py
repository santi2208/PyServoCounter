import sys
from ServoActions import *

class Servo(object):
    def __init__(self, actionUp, actionDown, gpio): 
        self.ActionUp = actionUp
        self.ActionDown = actionDown
        self.Gpio = gpio
        self.Estado = -1

    
    def Exec(self, posicion):
        servoActions = ServoActions()
        functionName = self.GetFunctionNameByPos(posicion)
        if(self.Estado != posicion):  
            getattr(servoActions,functionName)(self.Gpio)
        self.Estado = posicion
    
    def GetFunctionNameByPos(self, posicion):
        return self.ActionUp if posicion == 1 else self.ActionDown

    def SetState(self, estado):
        self.Estado = estado