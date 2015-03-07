#!/usr/bin/python3

import math
import cmath

class Media: # class definition
    def __init__(self,epsilon = float(1.0), mu = float(1.0), sigma = float(0.0),frequency = float(0.0)):
        self.epsilon = epsilon * (10**(-9)/(36*math.pi))
        self.mu = mu * (4*math.pi*10**(-7))
        self.sigma = sigma
        self.frequency = frequency
        self.alpha = self.frequency*math.sqrt(0.5*self.mu*self.epsilon*(math.sqrt(1+(self.sigma/(self.frequency*self.epsilon))**2) - 1))
        self.beta = self.frequency*math.sqrt(0.5*self.mu*self.epsilon*(math.sqrt(1+(self.sigma/(self.frequency*self.epsilon))**2) + 1))
        self.impedance = math.sqrt(self.mu/(self.frequency*(self.epsilon**2 + (self.sigma/self.frequency)**2)))*cmath.sqrt(self.frequency*self.epsilon + 1j*self.sigma)
    def setEpsilon(self,epsilon):
        self.epsilon = epsilon
    def setMu(self,mu):
        self.mu = mu
    def setSigma(self,sigma):
        self.sigma = sigma
    def setFrequency(self,frequency):
        self.frequency = frequency
    def getImpedance(self):
        return self.impedance
    def getGamma(self):
        Z = complex(self.alpha,self.beta)
        return Z

class Wave: # class definition
    def __init__(self, frequency = float(0.0), epsilon = float(1.0), mu = float(1.0), sigma = float(0.0)):
        self.module = 1.0
        self.frequency = (frequency * 2 * math.pi) # rad/m
        self.Media = Media(epsilon,mu,sigma,self.frequency)
        self.impedance = self.Media.getImpedance()
    def setFrequency(self,frequency):
        self.frequency = (frequency * 2 * math.pi)
        Media.setFrequency(self.frequency)
    def setEpsilon(self,epsilon):
        self.Media.setEpsilon(epsilon)
    def setMu(self,mu):
        self.Media.setMu(mu)
    def setSigma(self,sigma):
        self.Media.setSigma(sigma)
    def setModule(self,module):
        self.module = module
    def getFrequency(self):
        return self.frequency
    def getModule(self):
        return self.module
    def getGamma(self):
        return self.Media.getGamma()
    def getImpedance(self):
        return self.Media.getImpedance()


Pmi = 100.0
W1 = Wave(0.32*10**9)
W2 = Wave(0.32*10**9,80.0,1.0,5.0)
#
W1.setModule(cmath.sqrt(2*W1.getImpedance()*Pmi))
print("|Ei| = ",W1.getModule(),"|Hi| = ",W1.getModule()/W1.getImpedance())
#        
W1.setModule(cmath.sqrt(2*W1.getImpedance()*Pmi))
print("|Ei| = ",W1.getModule(),"|Hi| = ",W1.getModule()/W1.getImpedance())
#
print("Z1 = ",W1.getImpedance(),"=",abs(W1.getImpedance()),"phase",cmath.phase(W1.getImpedance())*180/math.pi)
print("Z2 = ",W2.getImpedance(),"=",abs(W2.getImpedance()),"phase",cmath.phase(W2.getImpedance())*180/math.pi)
#
Gamma_1 = W1.getGamma()
Gamma_2 = W2.getGamma()
print("Gamma_1 = ",Gamma_1,"=",abs(Gamma_1))
print("Gamma_2 = ",Gamma_2,"=",abs(Gamma_2),"phase",cmath.phase(Gamma_2)*180/math.pi)
#
coefc_R = (W2.getImpedance() - W1.getImpedance())/(W2.getImpedance() + W1.getImpedance())
coefc_R_abs = abs(coefc_R)
coefc_R_phase = cmath.phase(coefc_R)*180/math.pi
coefc_T = 2*W2.getImpedance()/(W2.getImpedance() + W1.getImpedance())
coefc_T_abs = abs(coefc_T)
coefc_T_phase = cmath.phase(coefc_T)*180/math.pi
print("Coefc_R = ",coefc_R,"=",coefc_R_abs,"phase",coefc_R_phase)
print("Coefc_T = ",coefc_T,"=",coefc_T_abs,"phase",coefc_T_phase)
#
print("|Er| = ",coefc_R_abs * W1.getModule(),"phase",coefc_R_phase + cmath.phase(W1.getModule())*180/math.pi)
print("|Hr| = ",coefc_R_abs * abs(W1.getModule()/W1.getImpedance()),"phase",coefc_R_phase + cmath.phase(1/W1.getImpedance())*180/math.pi)
#
print("|Et| = ",coefc_T_abs * W1.getModule(),"phase",coefc_T_phase + cmath.phase(W1.getModule())*180/math.pi)
print("|Ht| = ",coefc_T_abs * abs(W1.getModule()/W2.getImpedance()),"phase",coefc_T_phase + cmath.phase(1/W2.getImpedance())*180/math.pi)
#
Z1_R = W1.getImpedance().real
Z2_R = W2.getImpedance().real
Pmt = (Z2_R**(-1)*Pmi*(coefc_T_abs**2))/(Z1_R**(-1))
print("|Pmt| = ",Pmt)
