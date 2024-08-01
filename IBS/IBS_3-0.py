import numpy as np
import matplotlib.pyplot as plt
import os as OS
from classPredador import Predador 

#variaveis
Dimensions = 5.0

# Inicialização
coord = np.zeros((10,2))
presas = []
predadores = []

# Criando presa
def generate_Presa(numberOfIndividuals):
    for i in range(numberOfIndividuals):
        x = np.random.uniform(-Dimensions,Dimensions)
        y = np.random.uniform(-Dimensions,Dimensions)
        presas.append([x,y])

#criando Predador
def generate_Predador(numberOfIndividuals):
    for i in range(numberOfIndividuals):
        IdadePredador = np.random.randint(0,4)
        x = np.random.uniform(-Dimensions,Dimensions)
        y = np.random.uniform(-Dimensions,Dimensions)
        gender = np.random.randint(0,1)
        if gender == 1:
            gender = "M"
        else:
            gender = "F"
        predadores.append(Predador(gender,IdadePredador,[x,y]))

# Função decidir direção individuo 
def decide_direction(mov_max,mov_min):
    rlan = np.random.uniform(mov_min, mov_max)  #alcançe de movimento do individuo 
    theta = np.random.uniform(0, 2 * np.pi)
    return rlan * np.cos(theta), rlan * np.sin(theta) # Coordenada x e y a partir do centro

# Função mover individuo 
def move_individual(arrayIndividual,mov_max,mov_min):
    for individual in arrayIndividual:
        dx, dy = decide_direction(mov_max,mov_min)
        individual.coordenada = [individual.coordenada[0] + dx, individual.coordenada[1] + dy]


# Função para checar colisao
def check_colision_Presa(predador, presas, rp): 
    for i in predador:
        for j in presas:
            if np.sqrt((i.coordenada[0] - j[0])**2 + (i.coordenada[1] - j[1])**2) <= rp:
                return True
    return False   

# Função para checar colisao entre predadores
def check_colision_Predador(predador):
    for i in range(len(predador)):
        for j in range(i + 1, len(predador)): 
            valor_i = predador[i].coordenada
            valor_j = predador[j].coordenada
            print(valor_i,valor_j)

#set the number of individuals
generate_Predador(20)
generate_Presa(4)

print(len(predadores))
count = 0
while count < 50:
    # Plotagem do resultado
    move_individual(predadores,0.5,1.0)
    for i in predadores:
        if check_colision_Presa(predadores,presas,0.5):
            print("colide")
        print(check_colision_Predador(predadores))
        i.crescimento_predador()
    print(len(predadores))
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(111)
    ax1.scatter([predador.coordenada[0] for predador in predadores], [predador.coordenada[1] for predador in predadores], s=50, c='b')
    ax1.scatter([presa[0] for presa in presas], [presa[1] for presa in presas], s=150, c='r')
    plt.xlim(-Dimensions*3, Dimensions*3)  # Define limite fixo para o eixo x
    plt.ylim(-Dimensions*3, Dimensions*3)  # Define limite fixo para o eixo y
    plt.gca().set_aspect('equal', adjustable='box')  # Garante a proporção igual dos eixos
    plt.grid(True)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    count += 1
    
print(len(predadores))
    
OS.system("convert *.png ibs.gif && rm -rf *.png")
