from Predador import Predador
from classPrey import Prey

arrPrey = [Prey([1,5]),Prey([5,1])]
arrPred = [Predador("m",0,[1,5]),Predador("F",0,[1,5]),Predador("m",0,[5,1]),Predador("F",0,[5,1])]

for i in arrPrey:
    for j in arrPred:
        i.predators.append(j)


for i in arrPrey:
    print(i)