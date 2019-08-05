import numpy as np
import matplotlib.pyplot as plt
import  math as m

def Kolgomorov(arreglo):
    n = arreglo.size
    clases = m.ceil(m.sqrt(n))
    intervalos = np.array([])
    FrecuenciaObservada = np.zeros(clases)
    FrecuenciaObservadaA = np.array([])
    ProbalidadObservadaA = np.array([])
    ProbalidadEsperadaA = np.array([])
    Diferencia = np.array([])

    for i in range(1,clases+1):
        intervalos = np.append(intervalos,1/clases*i)

    ant=0
    for i in arreglo:
        for j in range(0,clases):
            if (i>=ant and i<intervalos[j]):
                FrecuenciaObservada[j]+=1
            ant=intervalos[j]
        ant=0

    FrecuenciaObservadaA = np.append(FrecuenciaObservadaA,FrecuenciaObservada[0])
    for i in range(1,clases):
        FrecuenciaObservadaA = np.append(FrecuenciaObservadaA, FrecuenciaObservadaA[i - 1] + FrecuenciaObservada[i])

    ProbalidadObservadaA = FrecuenciaObservadaA/n
    ProbalidadEsperadaA = intervalos

    for i in range(0,clases):
        Diferencia = np.append(Diferencia,abs(ProbalidadEsperadaA[i]-ProbalidadObservadaA[i]))

    XCalculado = np.max(Diferencia)
    Xcritico = 1.36/m.sqrt(n)

    #imprimo tabla
    print("intervalo  ","\t\t","FO      ","\t\t","FOA      ","\t\t","POA      ","\t\t","PEA      ","\t\t","Dife")
    for i in range(0,intervalos.size):
        print("%.5f" %intervalos[i],"\t\t",
              "%.5f" %FrecuenciaObservada[i],"\t\t",
              "%.5f" %FrecuenciaObservadaA[i],"\t\t",
              "%.5f" %ProbalidadObservadaA[i],"\t\t",
              "%.5f" %ProbalidadEsperadaA[i],"\t\t",
              "%.5f" %Diferencia[i])

    if XCalculado<=Xcritico:
        print("Xcal:",XCalculado,"<=  Xcrit:",Xcritico)
        print("Pasa la hipotesis")
    else:
        print("Xcal:", XCalculado, ">  Xcrit:", Xcritico)
        print("No pasa la hipotesis")




def GeneradorLineal(n):
    a = 100
    m = 165123
    c = 1234
    Xo = 32
    arreglo = np.array([])

    for i in range(0,n):
        Xn = (a*Xo+c) % m
        arreglo = np.append(arreglo,Xn)
        Xo=Xn


    return arreglo/m

num = 10000
Kolgomorov(GeneradorLineal(num))