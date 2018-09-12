from HttpProxy import HttpProxy

httpProxy = HttpProxy("http://localhost:8012/SetCounterState")
dtoToInform = [5, [1,1,1,0,0,0,1]]
httpProxy.InformServoStatus(dtoToInform)