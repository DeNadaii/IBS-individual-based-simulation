from Predador import Predador

Pred1 = Predador("m",0,[1,5])
Pred2 = Predador("m",0,[2,8])
Pred3 = Predador("m",0,[3,7])

# Exemplo de array de objetos
# objetos = [
#     {'id': 1, 'valores': [10, 20]},
#     {'id': 2, 'valores': [20, 30]},
#     {'id': 3, 'valores': [10, 30]},
# ]

objetos = [Pred1,Pred2,Pred3]

# Percorrer o array e comparar os atributos 'valores'
for i in range(len(objetos)):
    for j in range(i + 1, len(objetos)):  # Inicia j a partir de i + 1
        valor_i = objetos[i].coordenada
        valor_j = objetos[j].coordenada
        
        # Comparar os dois arrays de valores
        print(f'Comparando {valor_i} com {valor_j}')
