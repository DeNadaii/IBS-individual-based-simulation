import numpy as np
import matplotlib.pyplot as plt
import os as OS
import random
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
        IdadePredador = 1
        x = np.random.uniform(-Dimensions,Dimensions)
        y = np.random.uniform(-Dimensions,Dimensions)
        gender = ["M","F"]
        predadores.append(Predador(random.choice(gender),IdadePredador,[x,y]))

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

def death_control(arrPredadores):
    for i in arrPredadores:
        if i.idade == 4:
            arrPredadores.pop(i)

# Função para checar colisao entre predadores
def check_colision_Predador(predador,rp): #rp define a distancia de aproximação para o acasalamento
    for i in range(len(predador)):
        for j in range(i + 1, len(predador)): 
            valor_i = predador[i].coordenada
            valor_j = predador[j].coordenada
            sexo_i = predador[i].genero
            sexo_j = predador[j].genero
            idade_i = predador[i].apto_a_procriar()
            idade_j = predador[j].apto_a_procriar()
            #print("i", idade_i, "j", idade_j)
            if np.sqrt((valor_i[0] - valor_j[0])**2 + (valor_i[1] - valor_j[1])**2) <= rp and sexo_i != sexo_j and idade_i and idade_j:
                generate_Predador(1)
                return True
            

#set the number of individuals
generate_Predador(10)
generate_Presa(0)


count = 0
while count < 50:
    # Plotagem do resultado
    move_individual(predadores,0.5,1.0)
    print(count,check_colision_Predador(predadores,0.75),len(predadores))
    death_control(predadores)
    for i in predadores:
        i.crescimento_predador()
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
    

    
OS.system("convert *.png ibs.gif && rm -rf *.png")
