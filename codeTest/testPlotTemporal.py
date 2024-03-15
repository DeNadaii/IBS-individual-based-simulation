import matplotlib.pyplot as plt

arr = [1,1,1]
arr2 = [1,1,1,1,1]
arr3 = [1,1,]
arr4 = [1,1,1,1]
plt.plot([len(arr),len(arr2),len(arr3),len(arr4)])
plt.ylabel('some numbers')
plt.savefig("graficoTemporal/test2", bbox_inches='tight')
plt.show()