#!/usr/bin/python3 -q

import mpmath as mp
import ElectromagneticWave as EM

mp.dps = 5
mp.pretty = True
rad2deg = 180.0/mp.pi

Wi = EM.ElectroMagneticWave(freq = 5*10**9) # incident wave
Z1 = mp.mpc(Wi.getImpedance())
Wt = EM.ElectroMagneticWave(freq = 5*10**9,eps = 6,sig=2.5*10**(-3)) # transmitted auxiliar wave
Z2 = mp.mpc(Wt.getImpedance())

print("Z1",Z1,"Módulo de Z1", mp.fabs(Z1),"e fase",mp.arg(Z1))
print("Z2",Z2,"Módulo de Z2", mp.sqrt(Z2*mp.conj(Z2)),"e fase",mp.arg(Z2)*rad2deg)

RC = (Z2 - Z1)/(Z2 + Z1) # reflexion coeficient
TM = mp.re(RC) + 1 # transmition coeficient

Wt = EM.ElectroMagneticWave(wmod = TM*Wi.getElectricFieldModule(),freq = 5*10**9,eps = 6,sig=2.5*10**(-3)) # transmitted wave

print("Onda Incidente")
Wi.getElectricField()
Wi.getMagneticField()

print("Onda Transmitida")
Wt.getElectricField()
Wt.getMagneticField()

Pmi = 0.5/mp.re(Z1)
print("Modulo do vetor de Poynting Médio incidente.:",Pmi)

Pmr = 0.5*mp.re(RC)**2/mp.re(Z1)
print("Modulo do vetor de Poynting Médio refletido.:",Pmr)

Ppmr = Pmr/Pmi
print("Percentagem da energia refletida na interface.:%.2f" %(100*Ppmr),"%")

Pmt = 0.5*TM**2/Z2.real
print("Modulo do vetor de Poynting Médio transmitido.:",Pmt)

Ppmr = Pmt/Pmi
print("Percentagem da energia transmitida na interface.:%.2f" %(100*Ppmr),"%")
