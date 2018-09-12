import RPi.GPIO as GPIO
import time
# The script as below using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)

class ServoActions(object):
	def __init__(self):
		self.SleepTime = 0.5

	def Deg0(self, gpioPort):
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(12.5) 
		time.sleep(self.SleepTime)	
		pwm.stop()
		
	def Deg45(self, gpioPort):
		print('NotImplemented')
		
	def Deg90(self, gpioPort):
		print('90 Deg. Port: ' + str(gpioPort))
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	
		pwm.ChangeDutyCycle(7.5)
		time.sleep(self.SleepTime)			
		pwm.stop()
		
	def Deg135(self, gpioPort):
		print('NotImplemented')
		
	def Deg180(self, gpioPort):
		print('180 Deg. Port: ' + str(gpioPort))
		GPIO.setup(gpioPort,GPIO.OUT)
		pwm = GPIO.PWM(gpioPort,50) 
		pwm.start(7.5)	

		pwm.ChangeDutyCycle(2.5)		
		time.sleep(self.SleepTime)
		pwm.stop()
		
	def ScanOn(self, gpioPort):
		print('NotImplemented')
		
	def ScanOff(self, gpioPort):		
		print('NotImplemented')
	
	def GetDutyCycleByFunctionName(self, functionName):
		return 2.5 if functionName == "Deg180" else 7.5 if functionName == "Deg90" else 12.5

	def ExecuteMultipleActionsSync(self, gpioFunctionList):
		pwms = []
		#Start All
		for gf in gpioFunctionList:
			GPIO.setup(gf.Gpio, GPIO.OUT)
			pwm = GPIO.PWM(gf.Gpio,50) 
			pwm.start(7.5)	
			pwm.ChangeDutyCycle(self.GetDutyCycleByFunctionName(gf.FunctionName))
			pwms.append(pwm)

		time.sleep(self.SleepTime)

		#StopAll
		for pwm in pwms:
			pwm.stop()