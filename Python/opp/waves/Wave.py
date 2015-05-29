import mpmath as mp

class Wave: # wave class definition
    def __init__(self,module = mp.mpf(1.0),frequency = mp.mpf(0.0),phase = mp.mpf(0.0)):
        self.__module = module
        self.__phase = phase*(mp.pi/180.0) # rad
        self.__frequency = 2.0*mp.pi*frequency # rad/s
    # end of default constructor
    def setModule(self,value):
        self.__init__(module = value)
    def setFrequency(self,value):
        self.__frequency = 2.0*mp.pi*value # rad/s
    def setPhase(self,value):
        self.__phase = value*(mp.pi/180) # rad
    def getFrequency(self):
        return self.__frequency*0.5/mp.pi# hz
    def getModule(self):
        return self.__module
    def getPhase(self):
        return self.__phase*180.0/mp.pi # degrees
    def printWave(self):
        print("module = %.3f frequency = %.2f (Hz) phase = %.2f (degrees)" %
              (self.getModule(),self.getFrequency(),self.getPhase()))
