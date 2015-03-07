#!/bin/python3

import math
import cmath
import numpy as np

class ComplexNumbers: # class definition

    def __init__(self,r = float(0.0), i = float(0.0)): # default constructor
        self.real = r # data member
        self.img = i # data member

    def setReal(self,r):
        self.real = r
    def getReal(self):
        return self.real
    def setImg(self,i):
        self.img = i
    def getImg(self):
        return self.img
    def getPhase(self): # method which return a ComplexNumbers phase
        return cmath.phase(complex(self.getReal(),self.getImg()))
    def module(self): # method which return a ComplexNumbers modulus
        return math.sqrt(self.getReal()**2 + self.getImg()**2)    
    def Nroot(self,N = int(0)): # method which return nth root of a ComplexNumbers
        Z = np.zeros(N,dtype=np.complex)
        RO = self.module()**(1/N)
        THETA = self.getPhase()
        FRG = 180/math.pi
        for K in range(0,N):
            print("\n")
            Phi = (THETA + 2*K*math.pi)/N
            Z[K] = RO*complex(math.cos(Phi),math.sin(Phi))
            print("Z_2(K =",K,",","Phi =",Phi*FRG,")",Z[K])
        print("\n")
        for K in range(0,N):
            print(Z[K]**N - complex(self.getReal(),self.getImg()))
        return Z # return a vector of type complex which is the n-roots of a ComplexNumbers
    def __add__(self,value): # overload + operator
        soma = ComplexNumbers(self.getReal() + value.getReal(),self.getImg() + value.getImg())
        return soma
    def __sub__(self,value): # overload - operator
        subtracao = ComplexNumbers(self.getReal() - value.getReal(),self.getImg() - value.getImg())
        return subtracao
    def __mul__(self,value): # overload * operator
        multiplicacao = ComplexNumbers(self.getReal()*value.getReal() - self.getImg()*value.getImg(),self.getReal()*value.getImg() + self.getImg()*value.getReal())
        return multiplicacao
    def __truediv__(self,value): # overload / operator
        ZMULT = ComplexNumbers()
        ZMULT = self * conjugate(value)
        Z_MOD_2 = value.module()**2 
        divisao = ComplexNumbers(ZMULT.getReal()/Z_MOD_2,ZMULT.getImg()/Z_MOD_2) 
        return divisao
# End of ComplexNumbers Class


def conjugate(Z = ComplexNumbers()): # Return a conjugate of a ComplexNumbers
    Z_C = ComplexNumbers(Z.getReal(),Z.getImg()*(-1))
    return Z_C

def nroot(N = int(1),V = complex(0.0,0.0)): # Compute the nth root of a complex type
    Z = np.zeros(N,dtype=np.complex)
    RO = abs(V)**(1/N)
    THETA = cmath.phase(V)
    FRG = 180/math.pi
    for K in range(0,N):
        print("\n")
        Phi = (THETA + 2*K*math.pi)/N
        Z[K] = RO*complex(math.cos(Phi),math.sin(Phi))
        print("Z_2(K =",K,",","Phi =",Phi*FRG,")",Z[K])
    print("\n")
    for K in range(0,N):
        print(Z[K]**N - V)
    return Z

def argand(a): # Plot Point on Complex Plane
    import matplotlib.pyplot as plt
    import numpy as np
    for x in range(len(a)):
        plt.plot([0,a[x].real],[0,a[x].imag],'ro-',label='python')
    limit=np.max(np.ceil(np.absolute(a))) # set limits for axis
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()



Z1 = ComplexNumbers(3.5,2.1)
Z2 = ComplexNumbers(0,-2.5)
Z3 = ComplexNumbers(-2,1)
Z4 = Z3

print("\nZ1 criado com o construtor default \n Z1 = ",Z1.getReal(),'+ j',Z1.getImg())
print("Z2 criado com o construtor default \n Z2 = ",Z2.getReal(),'+ j',Z2.getImg())
ZMULT = Z1 * Z2
print("Produto de Z1 * Z2 \n ZMULT = ",ZMULT.getReal(),'+ j',ZMULT.getImg())
#
ZCONJ = conjugate(Z1)
print("ZCONJ complexo conjugado de Z1 \n ZCONJ = ",ZCONJ.getReal(),'+ j',ZCONJ.getImg())
ZMULT = Z1 * ZCONJ
print("Produto de Z1 * ZCONJ \n ZMULT = ",ZMULT.getReal(),'+ j',ZMULT.getImg())
#
print("Z3 criado com o construtor default \n Z3 = ",Z3.getReal(),'+ j',Z3.getImg())
print("Z4 criado com o construtor default \n Z4 = ",Z4.getReal(),'+ j',Z4.getImg())
ZDIV = Z3 / Z4
print("Divisão entre Z3 / Z4 \n ZDIV = ",ZDIV.getReal(),'+ j',ZDIV.getImg())

Z = ComplexNumbers(0,-1) # ComplexNumbers 0 - j0
U = Z.Nroot(5) # Return solutions of Z^5 + 1 = 0
argand(U) # Plot all solutions
