import math
import cmath

class Media: # media class definition
    def __init__(self,epsilon = float(1.0),mu = float(1.0),sigma = float(0.0)):
        self.__epsilon = epsilon * (10**(-9)/(36*math.pi)) # F/m
        self.__mu = mu * (4*math.pi*10**(-7)) # H/m
        self.__sigma = sigma # Siemens
        self.__impedance = math.sqrt(self.__mu/self.__epsilon)
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
    def getImpedance(self):
        return self.__impedance
    def printMedia(self):
        print("epsilon (F/m) = ",self.getEpsilon(),"mu (H/m) =",self.getMu(),
              "sigma (S)=",self.getSigma(),"impedance (ohms) =",self.getImpedance())

class Wave: # wave class definition
    def __init__(self,freq = float(0.0),mod = float(1.0),phs = float(0.0)):
        self.__module = mod
        self.__phase = phs*(math.pi/180) # rad
        self.__frequency = freq # Hz
    def setModule(self,value):
        self.__module = value
    def setFrequency(self,value):
        self.__frequency = value
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

class ElectroMagneticWave(Wave): # electromagnetic wave definition
    def __init__(self,e = float(1.0),m = float(1.0),s = float(1.0),mod = float(1.0),freq = float(1.0),phs = float(0.0)):
        self.__Media = Media(epsilon = e,mu = m,sigma = s)
        self.__electricfield = Wave(module = mod,frequency = freq,phase = phs)
        self.__magneticfield = Wave(module = (mod/self.__Media.getImpedance()),frequency = freq,phase = phs)
        #wave.setModule(self.__electricfield.getModule()/media.getImpedance())
    def getElectricField(self):
        print("Electric Field ->","module =",self.__electricfield.getModule(),
              "frequency =",self.__electricfield.getFrequency(),
              "phase =",self.__electricfield.getPhase())
    def getMagneticField(self):
        print("Magnectic Field ->","module =",self.__magneticfield.getModule(),
              "frequency =",self.__magneticfield.getFrequency(),
              "phase =",self.__magneticfield.getPhase())
