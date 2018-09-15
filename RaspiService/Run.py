import sys
import time
import argparse
from ServoActions import *
from InitialConfigs import *
from decimal import Decimal
from MainServoController import *
from HttpProxy import HttpProxy

class MainServoCounter(object):
    def __init__(self, httpProxy, servoActions, initialConfig, implementation, sleepTime, numero):
        self.httpProxy = httpProxy 
        self.servoActions = servoActions
        self.numeros = initialConfig.SetNumbers()
        self.Implementation = implementation if implementation is not None else 1
        self.numeroFijo = numero 
        self.SleepTime = sleepTime if sleepTime is not None else 2
        self.MainServoController = MainServoController()

    def RunService(self):
        print("Iniciando...")
        nums = self.numeros if self.numeroFijo is None else [self.numeros[self.numeroFijo]]
        for num in nums:
            if(self.httpProxy is not None):
                self.InformState(num)
            self.SetNumber(num)
            time.sleep(self.SleepTime)

    def SetNumber(self, num):
        print("-------NUMERO {} --------".format(num.Nombre))
        if(self.Implementation == 1):
            self.MainServoController.ExecuteAll(num.ServosPosiciones)
        else:
            for sPos in num.ServosPosiciones:
                sPos.Servo.Exec(sPos.Posicion)  
    
    def InformState(self, num):
        statesToInform = list(map(lambda x: x.Servo.Estado, num.ServosPosiciones))
        dtoToInform = [num.Id, statesToInform]
        print(dtoToInform)
        self.httpProxy.InformServoStatus(dtoToInform)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', help='0: Un servo a la vez || 1: Todos los servos al mismo tiempo - Default: 1')
    parser.add_argument('--num', help='Numero Fijo - Default: 0 - 9')
    parser.add_argument('--time', help='Sleep Time: Intervalo de espera entre numero y numero - Default: 0.8')
    parser.add_argument('--sIp', help='Ip del servidor.')
    parser.add_argument('--useWeb', help='Reporta estado a un servidor - Default: False')
    args = parser.parse_args()    
    
    implementation = int(args.all) if args.all is not None else 1
    sleepTime = Decimal(args.time) if args.time is not None else 0.8
    numero = int(args.num) if args.num is not None else None
    httpProxy = HttpProxy('http://{}:8012/SetCounterState'.format(args.sIp)) if args.sIp is not None else HttpProxy('http://192.168.0.18:8012/SetCounterState')
    sc = MainServoCounter(httpProxy if args.useWeb is not None else None, ServoActions(), InitialConfigs(), implementation, sleepTime, numero)
    sc.RunService()