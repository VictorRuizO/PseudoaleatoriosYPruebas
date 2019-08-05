import numpy as np
import  math as m

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

def Poker(numeros):
    FrecuenciaObservada = np.zeros(3)
    FrecuenciaEsperada = np.zeros(3)
    Diferencia = np.array([])
    for i in numeros:
        numero=i

        aux = i*10
        n1 = m.floor(aux)
        numero=aux-n1
        aux=numero*10
        n2=m.floor(aux)
        numero = aux-n2
        aux =numero*10
        n3 = m.floor(aux)
        #print(n1,n2,n3)

        if n1==n2 and n2==n3:
            FrecuenciaObservada[0]+=1
        elif n1==n2 or n1==n3 or n2==n3:
            FrecuenciaObservada[1]+=1
        else:
            FrecuenciaObservada[2]+=1


    FrecuenciaEsperada[0] = 0.01*numeros.size
    FrecuenciaEsperada[1] = 0.27*numeros.size
    FrecuenciaEsperada[2] = 0.72 * numeros.size

    Xcalculado =0
    for i in range(0,3):
        Diferencia = np.append(Diferencia, m.pow(FrecuenciaEsperada[i]-FrecuenciaObservada[i],2)/FrecuenciaEsperada[i])
        Xcalculado+=Diferencia[i]

    #Como son 3 clases, los grados de libertad son 2. Por lo tanto el Xcritico con 5% es
    Xcritico = 5.99
    clases = np.array(["3 cartas iguales","3 iguales 1 dif","3 diferentes    "])
    print("Clase\t\t\t\t\t","FO\t\t\t\t","FE\t\t\t\t","Error")
    for i in range(0,3):
        print(clases[i],"\t\t",
              "%.5f" %FrecuenciaObservada[i],"\t\t",
              "%.5f" %FrecuenciaEsperada[i],"\t\t",
              "%.5f" %Diferencia[i])

    if Xcalculado<=Xcritico:
        print("Xcal:",Xcalculado,"<=  Xcrit:",Xcritico)
        print("Pasa la hipotesis")
    else:
        print("Xcal:", Xcalculado, ">  Xcrit:", Xcritico)
        print("No pasa la hipotesis")


numeros = GeneradorLineal(1000)
Poker(numeros)


