class ServoExecVo(object):
    def __init__(self, gpioNumber, functionNameToExecute):
        self.Gpio = gpioNumber
        self.FunctionName = functionNameToExecute