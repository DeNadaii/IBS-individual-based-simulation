from Predador import Predador
from classPrey import Prey

Pred1 = Predador("m",0,[1,5])
print(Pred1.coordenada)
Pred1.coordenada = [2,5]
print(Pred1.coordenada)
prey1 = Prey([1,5],Pred1.coordenada)
print(prey1.predators[1])
