import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

L = 10

matrix = np.zeros((L, L))

coordenadas = []

index = 0
while index <= 10:
    coordenadas.append([index, index])
    print(coordenadas)
    index += 1

for i in coordenadas:
    if not i[0] or i[1] == L:
        matrix[i[0]][i[1]] = 1
    else:
        print("fora do limite")
 
cmapmine = ListedColormap(['w', 'b'], N=2)
plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=1)
plt.show()