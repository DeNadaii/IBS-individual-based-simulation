import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

L = 10

matrix = np.zeros((L, L))

coordenadasPresa = [[1,1],[2,2],[3,3],[4,4]]
coordenadasPredador = [[1,1],[2,5],[3,5],[4,6]]

# index = 0
# while index < 10:
#     coordenadas.append([index, index])
#     print(coordenadas)
#     index += 1

# for i in coordenadasPresa:
#     matrix[i[0]][i[1]] = 1

# count_i = 0
# for i in coordenadasPresa:
#     count_j = 0
#     for j in coordenadasPredador:
#         print("count_j: ",count_j)
#         count_j += 1
# print("count_i: ",count_i)
# count_i += 1
               
count_i = 0 
for i in coordenadasPresa:
    print("i",count_i)
    count_j = 0
    for j in coordenadasPredador:
        print("j",count_j)
        count_j += 1
    count_i += 1
        
cmapmine = ListedColormap(['w', 'b'], N=2)
plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=1)
# plt.show()