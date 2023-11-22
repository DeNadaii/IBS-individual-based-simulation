coordenadasPresa = [[1,1],[2,2],[3,3],[4,4]]
coordenadasPredador = [[1,1],[2,5],[3,5],[2,2]]

print(coordenadasPredador)
count = 0
for i in coordenadasPresa:
    for j in coordenadasPredador:
        if i == j:
            print(i)
            print(j)
            coordenadasPredador.pop(count)
count += 1
   
print(coordenadasPredador)