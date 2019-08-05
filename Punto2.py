import numpy as np
import matplotlib.pyplot as plt


def generador(arregloR):
    elements = [1, 3, 5, 7, 9, 11]
    probabilities = [0.2, 0.15, 0.15, 0.1, 0.25, 0.15]
    probabilitiesAcomuladas = np.array([])
    salida = np.array([])
    probabilitiesAcomuladas = np.append(probabilitiesAcomuladas,probabilities[0])
    for i in range(1,6):
        probabilitiesAcomuladas = np.append(probabilitiesAcomuladas,probabilitiesAcomuladas[i-1]+probabilities[i])

    print("a:", elements)
    print("p:", probabilities)
    print("pa:", probabilitiesAcomuladas)

    for i in arregloR:
        for j in range(0,6):
            if i<probabilitiesAcomuladas[j]:
                salida = np.append(salida,elements[j])
                print("r:", i)
                print("a:", elements[j],"\n")
                break

    return salida

randoms = np.random.random(1000)
salida = generador(randoms)
plt.hist(salida, density=True, bins=30)
plt.show()

elements = [1, 3, 5, 7, 9, 11]
probabilities = [0.2, 0.15, 0.15, 0.1, 0.25, 0.15]
numbers = np.random.choice(elements,1000,p=probabilities)
plt.hist(numbers, density=True, bins=30)
plt.show()



