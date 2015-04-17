import math
import cmath

class Media: # media class definition
    def __init__(self,epsilon = float(1.0),mu = float(1.0),sigma = float(0.0)):
        self.__epsilon = epsilon * (10**(-9)/(36*math.pi)) # F/m
        self.__mu = mu * (4*math.pi*10**(-7)) # H/m
        self.__sigma = sigma # Siemens        
    def setEpsilon(self,value):
        self.__epsilon = value * (10**(-9)/(36*math.pi))
    def setMu(self,value):
        self.__mu = value * (4*math.pi*10**(-7))
    def setSigma(self,value):
        self.__sigma = value
    def getEpsilon(self):
        return self.__epsilon
    def getMu(self):
        return self.__mu
    def getSigma(self):
        return self.__sigma
    def printMedia(self):
        print("epsilon (F/m) = ",self.getEpsilon(),"mu (H/m) =",self.getMu(),"sigma (S)=",self.getSigma())

class Wave: # wave class definition
    def __init__(self,module = float(1.0),frequency = float(0.0),phase = float(0.0)):
        self.__module = module
        self.__phase = phase*(math.pi/180) # rad
        self.__frequency = 2*math.pi*frequency # rad/s
    # end of default constructor
    def setModule(self,value):
        self.__init__(module = value)
    def setFrequency(self,value):
        self.__frequency = 2*math.pi*value # rad/s
    def setPhase(self,value):
        self.__phase = value*(math.pi/180) # rad
    def getFrequency(self):
        return self.__frequency
    def getModule(self):
        return self.__module
    def getPhase(self):
        return self.__phase # rad
    def printWave(self):
        print("frequency (rad/s) =",self.getFrequency(),"module =",self.getModule(),"phase (rad) =",self.getPhase())

class ElectroMagneticWave(): # electromagnetic wave definition
    def __init__(self,module = float(1.0),frequency = float(1.0),phase = float(0.0),epsilon = float(1.0),mu = float(1.0),sigma = float(0.0)):
        self.__Media = Media(epsilon = epsilon,mu = mu,sigma = sigma)
        self.__impedance = cmath.sqrt(1j*frequency*self.__Media.getMu()/(self.__Media.getSigma() + 1j*frequency*self.__Media.getEpsilon()))
        self.__electricfield = Wave(module = module,frequency = frequency,phase = phase)
        self.__magneticfield = Wave(module = (module/abs(self.__impedance)),frequency = frequency,phase = self.__electricfield.getPhase() + cmath.phase(self.__impedance))
        # end of default constructor
    def setEpsilon(self,value):
        self.__init__(module = self.__electricfield.getModule(),frequency = 0.5*self.__electricfield.getFrequency()/math.pi,phase = self.__electricfield.getPhase(),epsilon = value,mu = self.__Media.getMu(),sigma = self.__Media.getSigma())
    def setMu(self,value):
        self.__init__(module = self.__electricfield.getModule(),frequency = 0.5*self.__electricfield.getFrequency()/math.pi,phase = self.__electricfield.getPhase(),epsilon = self.__Media.getEpsilon(),mu = value,sigma = self.__Media.getSigma())
    def setSigma(self,value):
        self.__init__(module = self.__electricfield.getModule(),frequency = 0.5*self.__electricfield.getFrequency()/math.pi,phase = self.__electricfield.getPhase(),epsilon = self.__Media.getEpsilon(),mu = self.__Media.getMu(), sigma = value)
    def getMedia(self):
        self.__Media.printMedia()
    def getElectricField(self):
        radtograd = 180/math.pi
        print("Electric Field ->","module =",self.__electricfield.getModule(),
              "frequency =",self.__electricfield.getFrequency()*radtograd,
              "phase =",self.__electricfield.getPhase()*radtograd)
    def getMagneticField(self):
        radtograd = 180/math.pi
        print("Magnectic Field ->","module =",self.__magneticfield.getModule(),
              "frequency =",self.__magneticfield.getFrequency()*radtograd,
              "phase =",self.__magneticfield.getPhase()*radtograd)

W = ElectroMagneticWave(module = 10.0,frequency = 10**3,phase = 30.0,epsilon = 54.0,sigma = 3.9) # 10V e 100Hz
W.getMedia()
W.getElectricField()
W.getMagneticField()
W.setEpsilon(3.0)
W.getMedia()
W.getElectricField()
W.getMagneticField()
