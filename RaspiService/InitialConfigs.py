from Numero import Numero
from Servo import Servo
from ServoPos import ServoPos

class InitialConfigs(object):
    def __init__(self):
        self.Servos = self.SetServos()
        self.Posiciones = self.SetPosiciones()
    
    def SetNumbers(self):
        numbers = []
        i = 0
        for pos in self.Posiciones:
            numbers.append(self.SetNumber(i, "Numero {}".format(i), pos))
            i = i + 1
        
        return numbers
    
    def SetNumber(self, numberId, numberName, positions):
        pos = 0
        servosPos = []
        for servo in self.Servos:
            servosPos.append(ServoPos(servo, positions[pos]))
            pos = pos + 1
        return Numero(numberId, numberName, servosPos)
    
    def SetPosiciones(self):
        posiciones = []
        posiciones.append([1, 1, 1, 1, 1, 1, 0]) # 0
        posiciones.append([0, 1, 0, 1, 0, 0, 0]) # 1
        posiciones.append([1, 1, 0, 0, 1, 1, 1]) # 2
        posiciones.append([1, 1, 0, 1, 1, 0, 1]) # 3
        posiciones.append([0, 1, 1, 1, 0, 0, 1]) # 4
        posiciones.append([1, 0, 1, 1, 1, 0, 1]) # 5
        posiciones.append([1, 0, 1, 1, 1, 1, 1]) # 6
        posiciones.append([1, 1, 0, 1, 0, 0, 0]) # 7
        posiciones.append([1, 1, 1, 1, 1, 1, 1]) # 8
        posiciones.append([1, 1, 1, 1, 1, 0, 1]) # 9
        return posiciones
    
    def SetServos(self):
        servos = []
        servos.append(Servo('Deg0', 'Deg180', 2)) #SRV1
        servos.append(Servo('Deg180', 'Deg90', 3)) #SRV2
        servos.append(Servo('Deg90', 'Deg180', 4)) #SRV3
        servos.append(Servo('Deg180', 'Deg90', 14)) #SRV4
        servos.append(Servo('Deg180', 'Deg90', 15)) #SRV5
        servos.append(Servo('Deg90', 'Deg180', 18)) #SRV6
        servos.append(Servo('Deg180', 'Deg90', 23)) #SRV7
        return servos
        
