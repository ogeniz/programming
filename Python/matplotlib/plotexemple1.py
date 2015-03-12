#!/bin/python3

from numpy import *
import matplotlib.pyplot as plt

# sin(x) approx 


# x = linspace(0,2*pi,21)

# plt.plot(x,sin(x),'bo',label='sin(x)')
# plt.plot(x,cos(x),'r+',label='cos(x)')
# plt.legend()
# plt.show()


a,b = mgrid[-2:2:40j,-2:2:40j]
r = a**2 + b**2
f = sin(r)/r
plt.contourf(f)
plt.show()

# def mySin(X = float(0.0),N = int(1)):
#     result = X
#     n = N + 1
#     print(result)
#     for K in range(1,n):
#         if(K < N):            
#             result += ((-1)**K)*(X**(2*K + 1))/(math.factorial(2*K + 1))
#     return result

# print(mySin(pi/2,10))
