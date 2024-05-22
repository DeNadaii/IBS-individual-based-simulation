import numpy as np
import matplotlib.pyplot as plt
import os as OS
from classPredador import Predador 

#variaveis
Dimensions = 10.0

# Inicialização
coord = np.zeros((10,2))
predadores = []

#criando Predador
def generate_Predador():
    for i in range(10):
        IdadePredador = np.random.randint(0,4)
        x = np.random.uniform(-Dimensions,Dimensions)
        y = np.random.uniform(-Dimensions,Dimensions)
        predadores.append(Predador("M",IdadePredador,[x,y]))

# def generate_individual():
#     x = np.random.uniform(-Dimensions,Dimensions)
#     y = np.random.uniform(-Dimensions,Dimensions)
#     return x,y

# def popularMatriz():
#     for i in range(10):
#         x,y = generate_individual()
#         coord[i] = x,y


# Função mover individuo 
def decide_direction(mov_max,mov_min):
    rlan = np.random.uniform(mov_min, mov_max)  #alcançe de movimento do individuo 
    theta = np.random.uniform(0, 2 * np.pi)
    return rlan * np.cos(theta), rlan * np.sin(theta) # Coordenada x e ya partir do centro

def check_colision():
    return 0

generate_Predador()

count = 0
while count < 50:
    # Plotagem do resultado
        
    for predador in predadores:
        dx, dy = decide_direction(0.5, 1)
        predador.coordenada = [predador.coordenada[0] + dx, predador.coordenada[1] + dy]

    
    plt.figure(figsize=(10, 10))
    plt.scatter([predador.coordenada[0] for predador in predadores], 
                [predador.coordenada[1] for predador in predadores], 
                s=100)
    plt.xlim(-Dimensions, Dimensions)  # Define limite fixo para o eixo x
    plt.ylim(-Dimensions, Dimensions)  # Define limite fixo para o eixo y
    plt.gca().set_aspect('equal', adjustable='box')  # Garante a proporção igual dos eixos
    plt.grid(True)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("ResultadoImagens/matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("ResultadoImagens/matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    count += 1
    
OS.system("cd ResultadoImagens/ && convert *.png ibs.gif && rm -rf *.png")
