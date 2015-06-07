import mpmath as mp
import numpy as np
import ElectromagneticWave as EM

mp.dps=25
mp.pretty = True
theta_i = mp.radians(30)
cos_theta_i = mp.cos(theta_i)
sin_theta_i = mp.sin(theta_i)
E_i = 100*10**(-6) # [V/m]
f = 200*10**(6) # [Hz]

W_i = EM.ElectroMagneticWave(wmod=E_i,freq=f) # incident wave
W_t = EM.ElectroMagneticWave(freq=f,eps = 2.0) # auxiliar transmitted wave

g_1 = mp.mpc(W_i.getAlpha(),W_i.getBeta()) # gamma_1 real number
g_2 = mp.mpc(W_t.getAlpha(),W_t.getBeta()) # gamma_2 complex number
n_g_1 = mp.norm(g_1)
n_g_2 = mp.norm(g_2)
theta_t = mp.asin(n_g_1*sin_theta_i/n_g_2) # theta transmitted

den_cte = cos_theta_i + mp.sqrt(2)*mp.sqrt(1 - 0.5*sin_theta_i**2)
G = (cos_theta_i - (mp.sqrt(2)*mp.sqrt(1 - 0.5*sin_theta_i**2)))/den_cte
T = 2*cos_theta_i/den_cte

W_r = EM.ElectroMagneticWave(wmod=W_i.getElectricFieldModule()*mp.norm(G),freq=f) # reflected  wave
W_t = EM.ElectroMagneticWave(wmod=W_i.getElectricFieldModule()*T,freq=f,eps=2) # transmitted wave



print('ângulo de transmissão theta_t =',mp.degrees(theta_t))
print('Coeficiente de Reflexão G =',G)
print('Coeficiente de Transmissão T =',T)
print('*********************')
print('Onda incidente')
W_i.getElectricField()
W_i.getMagneticField()
print('*********************')
print('Onda Refletida')
W_r.getElectricField()
W_r.getMagneticField()
print('*********************')
print('Onda Transmitida')
W_t.getElectricField()
W_t.getMagneticField()
print('*********************')
