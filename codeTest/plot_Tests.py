import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

matrix = np.zeros((10,10))

i = 0
while i < 10:
    matrix[0][i] = 1
    print(matrix)
    cmapmine = ListedColormap(['w','b'], N=2)
    plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=2)
    plt.savefig("matrixTest{}.png".format(i), bbox_inches='tight') 
    i+=1

