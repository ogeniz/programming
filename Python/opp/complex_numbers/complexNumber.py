
import cmath
from math import *

class complexNumber(complex): # complexNumber class child of complex class basic type.
    def __init__(self,real = float(0.0),imag = float(0.0)):
        complex.__init__(real,imag)
        self.__module = abs(self)
        self.__phase = cmath.phase(self)
    def __str__(self):
        return complex.__str__(self)
    def getPhase(self):
        return self.__phase
    def getModule(self):
        return self.__module
    def phaseG(self):
        return self.__phase * 180/pi
    def polar(self):
        print("(modulo,phase) = (",self.__module,self.phaseG(),")")
    def __add__(self,value):
        return complexNumber(complex.__add__(self,value))
    def __sub__(self,value):
        return complexNumber(complex.__sub__(self,value))
    def __mul__(self,value):
        return complexNumber(complex.__mul__(self,value))
    def __truediv__(self,value):
        return complexNumber(complex.__truediv__(self,value))

def mp(Z1 = complexNumber(), Z2 = complexNumber()):
    if(not (Z2.getModule()) ):
        print("Divisão por Zero")
        return
    else:
        return (Z1.getModule()*Z2.getModule())*complexNumber(cos(Z1.getPhase()+Z2.getPhase()),sin(Z1.getPhase()+Z2.getPhase()))

def dp(Z1 = complexNumber(), Z2 = complexNumber()):
    if(not (Z2.getModule()) ):
        print("Divisão por Zero")
        return
    else:
        return (Z1.getModule()/Z2.getModule())*complexNumber(cos(Z1.getPhase()-Z2.getPhase()),sin(Z1.getPhase()-Z2.getPhase()))
