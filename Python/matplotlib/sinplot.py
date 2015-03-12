#!/usr/bin/python3

import cmath
from pylab import figure, show
from numpy import arange, sin, pi

fig = figure(1)

t = arange(-1.0, 1.0, 0.001)
fv = 1.0 # hertz
w = 2*pi*fv
L = 1 # henrys
C = 1 # faraday
RL = 1j*w*L # reatância em ohms
RC = 1/(1j*w*C)
RE = 0 # resistência em ohms
Re = RE + RL + RC# reatância equivalente em ohms
V = 220*sin(w*t) # volts
I = (220/abs(Re))*sin(w*t + cmath.phase(Re)) # amperes

ax1 = fig.add_subplot(211)
ax1.plot(t,V)
ax1.grid(True)
ax1.set_ylim((-250,250))
ax1.set_ylabel('Volts')
ax1.set_title('Tensão AC')
for label in ax1.get_xticklabels():
    label.set_color('r')

ax2 = fig.add_subplot(212)
ax2.plot(t,I)
ax2.grid(True)
ax2.set_ylim((-50,50))
ax2.set_ylabel('Àmperes')
ax2.set_title('Corrente AC')
for label in ax2.get_xticklabels():
    label.set_color('b')
    
show()

# t = arange(0.0, 1.0, 0.001)

# fig = figure(1)

# ax1 = fig.add_subplot(311)
# ax1.plot(t, sin(2*pi*t))
# ax1.grid(True)
# ax1.set_ylim( (-2,2) )
# ax1.set_ylabel('1 Hz')
# ax1.set_title('A sine wave or two')

# for label in ax1.get_xticklabels():
#     label.set_color('r')

# u = arange(0.0, 1.0, 0.001)

# ax2 = fig.add_subplot(312)
# ax2.plot(u, sin(60*2*pi*t - pi*0.5))
# ax2.grid(True)
# ax2.set_ylim( (-2,2) )
# l = ax2.set_xlabel('Hi mom')
# l.set_color('g')
# l.set_fontsize('large')

# u = arange(0.0, 1.0, 0.001)
# ka = 0.5

# ax3 = fig.add_subplot(313)
# ax3.plot(u, (1 + ka*sin(2*pi*t))*sin(60*2*pi*t - pi*0.5))
# ax3.grid(True)
# ax3.set_ylim( (-2,2) )
# l = ax3.set_xlabel('Hi mom')
# l.set_color('g')
# l.set_fontsize('large')kkkk
