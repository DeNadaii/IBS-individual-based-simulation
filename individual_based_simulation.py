import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os as OS


L = 100

matrix = np.zeros((L, L))

coordenadasPredadores = []
coordenadasPresas = []

def DirecaoPredador(a,b,index):
    DecidirDirecao = np.random.randint(0, 3)
    #Predador vermelho (2)
    #print("index predador", index)

    if DecidirDirecao == 0:                                         #move para baixo
        #print("MOVEU PARA CIMA")
        if not a-1 < 0:
            coordenadasPredadores[index] = [a-1,b]
        else:
            coordenadasPredadores[index] = [len(matrix)-1,b]
    if DecidirDirecao == 1:                                         #move para cima                                       
        #print("MOVEU PRA BAIXO")
        if not a+1 == len(matrix):
            coordenadasPredadores[index] = [a+1,b]
        else:
            coordenadasPredadores[index] = [0,b]
    if DecidirDirecao == 2:                                         #move para esquerda
        #print("MOVEU PRA ESQUERDA")
        if not b+1 == len(matrix[0]):
            coordenadasPredadores[index] = [a,b+1]
        else:
            coordenadasPredadores[index] = [a,0]
    if DecidirDirecao == 3:                                         #move para direita
        #print("MOVEU PRA DIREITA")
        if not b-1 < 0:
            coordenadasPredadores[index] = [a,b-1]
        else:
            coordenadasPredadores[index] = [a,len(matrix)-1]

def DirecaoPresa(a,b,index):
    DecidirDirecao = np.random.randint(0, 3)
    #Presa azul (1)
    #print("index presa", index)

    if DecidirDirecao == 0:                                         #move para cima
        #print("MOVEU PARA CIMA")
        if not a-1 < 0:
            coordenadasPresas[index] = [a-1,b]
        else:
            coordenadasPresas[index] = [len(matrix)-1,b]
    if DecidirDirecao == 1:                                         #move para baixo                                      
        #print("MOVEU PRA BAIXO")
        if not a+1 == len(matrix):
            coordenadasPresas[index] = [a+1,b]
        else:
            coordenadasPresas[index] = [0,b]
    if DecidirDirecao == 2:                                         #move para esquerda
        #print("MOVEU PRA ESQUERDA")
        if not b+1 == len(matrix[0]):
            coordenadasPresas[index] = [a,b+1]
        else:
            coordenadasPresas[index] = [a,0]
    if DecidirDirecao == 3:                                         #move para direita
        #print("MOVEU PRA DIREITA")
        if not b-1 < 0:
            coordenadasPresas[index] = [a,b-1]
        else:
            coordenadasPresas[index] = [a,len(matrix)-1]
            

def gerarPresa():
    gerar_Presa_x = np.random.randint(0, L-1)
    gerar_Presa_y = np.random.randint(0, L-1)
 
    if matrix[gerar_Presa_y][gerar_Presa_x] != 1:
        matrix[gerar_Presa_y][gerar_Presa_x] = 1
        
    coordenadasPresas.append([gerar_Presa_y,gerar_Presa_x])

    
    # print("presa x:", gerar_Presa_x, "presa y:", gerar_Presa_y)


def gerarPredador():
    gerar_Predador_x = np.random.randint(0, L-1)
    gerar_Predador_y = np.random.randint(0, L-1)
 
    if matrix[gerar_Predador_y][gerar_Predador_x] != 2:
        matrix[gerar_Predador_y][gerar_Predador_x] = 2
    
    coordenadasPredadores.append([gerar_Predador_y,gerar_Predador_x])
    # print("presa x:", gerar_Presa_x, "presa y:", gerar_Presa_y)


def popularMatriz():
    i = 0
    while i < 10:    
        gerarPresa()   
        gerarPredador() 
        i += 1
            
# popularMatriz()

def moverPredador():
    indexPredador = 0
    for i in coordenadasPredadores:                                                                  #decide direcao e move os predadores
        # print("coordenadasPredadores",coordenadasPredadores)
        # print("i",i)
        DirecaoPredador(i[0],i[1],indexPredador)
        matrix[i[0]][i[1]] = 0                                                                        #apaga a posicao anterior
        indexPredador += 1
    for j in coordenadasPredadores:                                                                  #preenche a nova posicao
        # print("j: ",j[0],j[1])
        matrix[j[0]][j[1]] = 2
        

def moverPresa():
    indexPresa = 0
    for i in coordenadasPresas:
        # print("coordenadasPresas",coordenadasPresas)
        # print("i",i)
        DirecaoPresa(i[0],i[1],indexPresa)
        matrix[i[0]][i[1]] = 0
        # print(i[0],i[1])
        # print("matriz", matrix[i[0]][i[1]])
        indexPresa += 1        
    for j in coordenadasPresas:
        # print("j:",j[0],j[1])
        matrix[j[0]][j[1]] = 1

popularMatriz()

def checaColisaoOld():
    count = 0
    for i in coordenadasPredadores:
        for j in coordenadasPresas:
            if i == j:
                print("i: ",i,"j: ",j)
                print("engual")
                coordenadasPresas.pop(count)
                coordenadasPredadores.insert(count,[i[0],i[1]])
    count += 1
    
def checaColisao():
    count_i = 0 
    for i in coordenadasPredadores:
        count_j = 0
        for j in coordenadasPresas:
            if i == j:
                print("engual")
                print(count_i,coordenadasPredadores)
                coordenadasPresas.pop(count_j)
                coordenadasPredadores.insert(count_i,[i[0],i[1]])
                print(count_i,coordenadasPredadores)
            count_j += 1
        count_i += 1
    
    
    
    
print("predador",len(coordenadasPredadores))
print("Presa",len(coordenadasPresas))
count = 0
while count < 100:
    print(count)
    moverPredador()
    moverPresa()
    checaColisao()
    cmapmine = ListedColormap(['w','b','r'], N=3)
    plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=2)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("ResultadoImagens/matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("ResultadoImagens/matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    count += 1

print("predador",len(coordenadasPredadores))
print("Presa",len(coordenadasPresas))


OS.system("cd ResultadoImagens/ && convert *.png ibs.gif && rm -rf *.png")


