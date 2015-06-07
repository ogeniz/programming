import mpmath as mp
import Wave as WV
import Media as MD

class ElectroMagneticWave(): # electromagnetic wave definition    
    def __init__(self,wmod = mp.mpf(1.0),freq = mp.mpf(1.0),phs = mp.mpf(0.0),eps = mp.mpf(1.0),mur = mp.mpf(1.0),sig = mp.mpf(0.0)):
        omega = 2*mp.pi*freq   # converts hz to rad/s
        self.__Media = MD.Media(epsilon = eps,mu = mur,sigma = sig)
        self.__impedance = mp.sqrt(self.__Media.getMu()/(self.__Media.getEpsilon() - mp.mpc(0,(self.__Media.getSigma()/omega))))
        self.__tanperca = mp.atan(self.__Media.getSigma()/(omega*self.__Media.getEpsilon()))
        anb_cte = omega*mp.sqrt(self.__Media.getMu()*self.__Media.getEpsilon()*mp.sec(self.__tanperca)) # constant to alpha and beta calculation
        self.__alpha = anb_cte*mp.sin(self.__tanperca*0.5) # alpha constant
        self.__beta = anb_cte*mp.cos(self.__tanperca*0.5) # beta constant
        self.__electricfield = WV.Wave(module = wmod,frequency = freq,phase = phs)
        self.__magneticfield = WV.Wave(module = wmod/mp.norm(self.__impedance),frequency = freq,phase = (self.__electricfield.getPhase() + mp.degrees(mp.arg(self.__impedance))))
        # end of default constructor
    def setEpsilon(self,value):
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = value,mur = self.__Media.getMur(),sig = self.__Media.getSigma())
    def setMu(self,value):        
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = self.__Media.getEpsilonr(),mur = value,sig = self.__Media.getSigma())        
    def setSigma(self,value):
        self.__init__(wmod = self.__electricfield.getModule(),freq = self.__electricfield.getFrequency(),phs = self.__electricfield.getPhase(),eps = self.__Media.getEpsilonr(),mur = self.__Media.getMur(), sig = value)
    def getAlpha(self):
        return self.__alpha
    def getBeta(self):
        return self.__beta
    def getTanPerca(self):
        return mp.degrees(self.__tanperca)
    def getMedia(self):
        self.__Media.printMedia()
    def getImpedance(self):
        return self.__impedance
    def getElectricFieldModule(self):
        return self.__electricfield.getModule()
    def getMagnecticFieldModule(self):
        return self.__magneticfield.getModule()
    def getElectricField(self):        
        print("Electric Field Módulo (V/m)")
        self.__electricfield.printWave()
        print("alpha = %f (Np/m) beta = %f (rad/m) tanlost = %f (degrees)" %
              (self.__alpha,self.__beta,mp.degrees(self.__tanperca)))
    def getMagneticField(self):
        print("Magnectic Field Módulo (A/m)")
        self.__magneticfield.printWave()
        print("alpha = %f (Np/m) beta = %f (rad/m) tanlost = %f (degrees)" %
              (self.__alpha,self.__beta,mp.degrees(self.__tanperca)))
