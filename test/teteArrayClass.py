from Predador import Predador
import numpy as np

Pred0 = Predador("m",0,[1,5])
Pred1 = Predador("m",0,[2,8])
Pred2 = Predador("m",0,[1,5])


objetos = [Pred0,Pred1,Pred2]

def add_Predador():
    x = np.random.randint(-5,5)
    y = np.random.randint(-5,5)
    objetos.append(Predador("m",0,[x,y]))    

# Exemplo de array de objetos
# objetos = [
#     {'id': 1, 'valores': [10, 20]},
#     {'id': 2, 'valores': [20, 30]},
#     {'id': 3, 'valores': [10, 30]},
# ]

print(len(objetos))
add_Predador()
print(len(objetos))

# Percorrer o array e comparar os atributos 'valores'
for i in range(len(objetos)):
    for j in range(i + 1, len(objetos)):  # Inicia j a partir de i + 1
        valor_i = objetos[i].coordenada
        valor_j = objetos[j].coordenada
        if valor_i == valor_j:
            print()
            add_Predador()
            True
            

for i in objetos:
    print(i.coordenada)

        
        
