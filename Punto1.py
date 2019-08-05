import numpy as np
import math as m
import matplotlib.pyplot as plt

def Exponencial(arreglo):
    ArregloSalida = np.array([])
    for i in arreglo:
        Num = -5*m.log(i)
        ArregloSalida = np.append(ArregloSalida,Num)

    return ArregloSalida


def GEM(n,semilla):
    arreglo = np.array([])
    Xn1 = semilla
    for i in range(0,n):
        Xn = (16806*Xn1) % 2147483647
        #Xn=Xn/2147483647
        arreglo = np.append(arreglo,Xn)
        Xn1 = Xn

    arreglo=arreglo/2147483647
    return arreglo



arreglo = GEM(10000,1)
x = Exponencial(arreglo)
y = np.random.exponential(5,10000)
plt.hist(x, density=True, bins=50)
plt.show()
plt.hist(y, density=True, bins=50)
plt.show()

