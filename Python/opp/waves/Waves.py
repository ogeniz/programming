import math
import cmath

class Media: # media class definition
    def __init__(self,epsilon = float(1.0),mu = float(1.0),sigma = float(0.0)):
        self.__epsilon = epsilon * (10**(-9)/(36.0*math.pi)) # F/m
        self.__mu = mu * (4.0*math.pi*10**(-7)) # H/m
        self.__sigma = sigma # Siemens        
    def setEpsilon(self,value):
        self.__epsilon = value * (10**(-9)/(36.0*math.pi)) # F/m
    def setMu(self,value):
        self.__mu = value * (4.0*math.pi*10**(-7)) # H/m
    def setSigma(self,value):
        self.__sigma = value # Siemens
    def getEpsilonr(self):
        return self.__epsilon/(10**(-9)/(36.0*math.pi)) # e_r
    def getEpsilon(self):
        return self.__epsilon
    def getMur(self):
        return self.__mu/(4.0*math.pi*10**(-7)) #mu_r
    def getMu(self):
        return self.__mu
    def getSigma(self):
        return self.__sigma
    def printMedia(self):
        print("epsilon (F/m) = %.1f e0 mu (H/m) = %.1f mu0 sigma = %.1f (Siemens)" %
              (self.getEpsilonr(),self.getMur(),self.getSigma()))

class Wave: # wave class definition
    def __init__(self,module = float(1.0),frequency = float(0.0),phase = float(0.0)):
        self.__module = module
        self.__phase = phase*(math.pi/180.0) # rad
        self.__frequency = 2.0*math.pi*frequency # rad/s
    # end of default constructor
    def setModule(self,value):
        self.__init__(module = value)
    def setFrequency(self,value):
        self.__frequency = 2.0*math.pi*value # rad/s
    def setPhase(self,value):
        self.__phase = value*(math.pi/180) # rad
    def getFrequency(self):
        return self.__frequency*0.5/math.pi# hz
    def getModule(self):
        return self.__module
    def getPhase(self):
        return self.__phase*180.0/math.pi # degrees
    def printWave(self):
        print("module = %.3f frequency = %.2f (Hz) phase = %.2f (degrees)" %
              (self.getModule(),self.getFrequency(),self.getPhase()))

class ElectroMagneticWave(): # electromagnetic wave definition    
    def __init__(self,wmod = float(1.0),freq = float(1.0),phs = float(0.0),eps = float(1.0),mur = float(1.0),sig = float(0.0)):
        rad2dgr = 180.0/math.pi
        omega = 2*math.pi*freq
        self.__Media = Media(epsilon = eps,mu = mur,sigma = sig)
        self.__impedance = cmath.sqrt(1j*freq*self.__Media.getMu()/(self.__Media.getSigma() + 1j*freq*self.__Media.getEpsilon()))
        self.__alpha =  omega*math.sqrt( (0.5*self.__Media.getMu()*self.__Media.getEpsilon()) * (math.sqrt(1+(self.__Media.getSigma()/(omega*self.__Media.getEpsilon()))**2) - 1) )
        self.__beta =  omega*math.sqrt( (0.5*self.__Media.getMu()*self.__Media.getEpsilon()) * (math.sqrt(1+(self.__Media.getSigma()/(omega*self.__Media.getEpsilon()))**2) + 1) )
        self.__tanperca = math.atan(self.__Media.getSigma()/(freq*self.__Media.getEpsilon()))
        self.__electricfield = Wave(module = wmod,frequency = freq,phase = phs)
        self.__magneticfield = Wave(module = (wmod/abs(self.__impedance)),frequency = freq,phase = (self.__electricfield.getPhase() + cmath.phase(self.__impedance)*rad2dgr))
        # end of default constructor
    def setEpsilon(self,value):
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = value,mur = self.__Media.getMur(),sig = self.__Media.getSigma())
    def setMu(self,value):        
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = self.__Media.getEpsilonr(),mur = value,sig = self.__Media.getSigma())        
    def setSigma(self,value):
        rad2dgr = 180.0/math.pi
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = self.__Media.getEpsilonr(),mur = self.__Media.getMur(), sig = value)
    def getAlpha(self):
        return self.__alpha
    def getBeta(self):
        return self.__beta
    def getTanPerca(self):
        return self.__tanperca*180.0/math.pi
    def getMedia(self):
        self.__Media.printMedia()
    def getImpedance(self):
        return self.__impedance
    def getElectricField(self):        
        print("Electric Field Módulo (V/m)")
        self.__electricfield.printWave()
        print("alpha = %.2f (Np/m) beta = %.2f (rad/m) tanlost = %.2f (degrees)" %
              (self.__alpha,self.__beta,self.__tanperca))
    def getMagneticField(self):
        print("Magnectic Field Módulo (A/m)")
        self.__magneticfield.printWave()
        print("alpha = %.2f (Np/m) beta = %.2f (rad/m) tanlost = %.2f (degrees)" %
              (self.__alpha,self.__beta,self.__tanperca))
    

W = ElectroMagneticWave(freq = 2*math.pi*10**7,eps = 81,sig = 4)
W.getElectricField()
pp = (W.getAlpha()**(-1)*0.001)/0.3679
print(pp)
