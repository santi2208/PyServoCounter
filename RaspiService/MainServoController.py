from ServoActions import *
from ServoExecVo import ServoExecVo

class MainServoController(object):
	def __init__(self):
		self.ServoExecVos = []
		self.ServoActions = ServoActions()
	
	def ExecuteAll(self, servosPos):
		for sPos in servosPos:
			pos = sPos.Posicion
			if(sPos.Servo.Estado != pos):
				self.ServoExecVos.append(ServoExecVo(sPos.Servo.Gpio, sPos.Servo.GetFunctionNameByPos(pos)))
				print("Servo {} moved...".format(sPos.Servo.Gpio))
			sPos.Servo.SetState(pos)
		self.ServoActions.ExecuteMultipleActionsSync(self.ServoExecVos)