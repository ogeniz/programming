import mpmath as mp

class Media: # media class definition
    def __init__(self,epsilon = mp.mpf(1.0),mu = mp.mpf(1.0),sigma = mp.mpf(0.0)):
        self.__epsilon = epsilon * (10**(-9)/(36.0*mp.pi)) # F/m
        self.__mu = mu * (4.0*mp.pi*10**(-7)) # H/m
        self.__sigma = sigma # Siemens        
    def setEpsilon(self,value):
        self.__epsilon = value * (10**(-9)/(36.0*mp.pi)) # F/m
    def setMu(self,value):
        self.__mu = value * (4.0*mp.pi*10**(-7)) # H/m
    def setSigma(self,value):
        self.__sigma = value # Siemens
    def getEpsilonr(self):
        return self.__epsilon/(10**(-9)/(36.0*mp.pi)) # e_r
    def getEpsilon(self):
        return self.__epsilon
    def getMur(self):
        return self.__mu/(4.0*mp.pi*10**(-7)) #mu_r
    def getMu(self):
        return self.__mu
    def getSigma(self):
        return self.__sigma
    def printMedia(self):
        print("epsilon (F/m) = %.1f e0 mu (H/m) = %.1f mu0 sigma = %.1f (Siemens)" %
              (self.getEpsilonr(),self.getMur(),self.getSigma()))
