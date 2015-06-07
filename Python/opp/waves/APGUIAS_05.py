import mpmath as mp
import numpy as np
import ElectromagneticWave as EM

mp.dps=25
mp.pretty = True
theta_i = mp.radians(30)
cos_theta_i = mp.cos(theta_i)
sin_theta_i = mp.sin(theta_i)

e_i = np.array([mp.cos(theta_i),0.0,mp.sin(theta_i)],dtype=mp.mpf)
h_i = np.array([0.0,1.0,0.0],dtype=mp.mpf)


W_i = EM.ElectroMagneticWave(wmod=5*10**(-4),freq=2*10**5) # incident wave
W_t = EM.ElectroMagneticWave(freq=2*10**5,eps = 80.0,sig = 3) # auxiliar transmitted wave

g_1 = mp.mpc(W_i.getAlpha(),W_i.getBeta()) # gamma_1 real number
g_2 = mp.mpc(W_t.getAlpha(),W_t.getBeta()) # gamma_2 complex number
n_g_1 = mp.norm(g_1)
n_g_2 = g_2.real
theta_t = mp.asin(n_g_1*sin_theta_i/n_g_2) # theta transmitted
cos_theta_t = mp.cos(theta_t)
sin_theta_t = mp.sin(theta_t)
Z1 = W_i.getImpedance()
Z2 = W_t.getImpedance()

n_Z1 = mp.norm(Z1)
n_Z2 = mp.norm(Z2)

G = (n_Z2*cos_theta_t - n_Z1*cos_theta_i)/(n_Z2*cos_theta_t + n_Z1*cos_theta_i)
T = (2*n_Z2*cos_theta_i)/(n_Z2*cos_theta_t + n_Z1*cos_theta_i)

W_r = EM.ElectroMagneticWave(wmod=5*10**(-4)*mp.norm(G),freq=2*10**5) # reflected  wave
W_t = EM.ElectroMagneticWave(wmod = W_i.getElectricFieldModule()*T,freq=2*10**5,eps = 80.0,sig = 3) # transmitted wave

print('Reflextion Coeficient G =',G)
print('Transmittion Coeficient T =',T)
print('Reflected Wave')
W_r.getElectricField()
W_r.getMagneticField()
print('Transmitted Wave')
W_t.getElectricField()
W_t.getMagneticField()

print('sin(theta_t) =',mp.norm(g_1/g_2)*sin_theta_i)
print('theta_t =',theta_t)
print('Ângulo de Transmissão theta_t =',mp.degrees(theta_t))
print('Z1 =',n_Z1,',','Z2 =',n_Z2)

print('%.5f'%(W_r.getElectricFieldModule()+W_t.getElectricFieldModule()))
