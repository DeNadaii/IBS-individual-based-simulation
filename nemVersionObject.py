import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os as OS


L = 50

matrix = np.zeros((L, L))

coordenadasPredadores = []
coordenadasPresas = []


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
    while i < 5:    
        gerarPresa()   
        gerarPredador() 
        i += 1


print("Predadores: ", coordenadasPredadores)
print("Presas: ", coordenadasPresas)
popularMatriz()
print("Predadores: ", coordenadasPredadores)
print("Presas: ", coordenadasPresas)

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
        

def decidirDireçãoGeral(arrEnd, tipo):
    n = np.random.randint(0,2) 
    p = np.random.randint(0,2)
    # print("p: ", p)
    # print("n: ", n)
    matrix[arrEnd[0]][arrEnd[1]] = 0
    print("antes", arrEnd)
    if p == 0:
        delta = (-1)**n
        arrEnd[1] += delta
        if arrEnd[1] < 0 or arrEnd[1] > (L-1):
            print("fora da borda pela pra cima ou pra baixo")
        if arrEnd[1] > (L-1):
            arrEnd[1] = 0
            print("depois EIXO Y", arrEnd)
        if arrEnd[1] < 0:
            arrEnd[1] = (L-1)
            print("depois EIXO Y", arrEnd)
        if tipo == "presa":
            matrix[arrEnd[0]][arrEnd[1]] = 1
        else:
            matrix[arrEnd[0]][arrEnd[1]] = 2
    else:
        delta = (-1)**n
        arrEnd[0] += delta
        if arrEnd[0] < 0 or arrEnd[0] > (L-1):
            print("fora da borda pelo esquerda ou direita")
        if arrEnd[0] > (L-1):
            arrEnd[0] = 0
            print("depois EIXO X", arrEnd)
        if arrEnd[0] < 0:
            arrEnd[0] = (L-1)
            print("depois EIXO X", arrEnd)
        if tipo == "presa":
            matrix[arrEnd[0]][arrEnd[1]] = 1
        else:
            matrix[arrEnd[0]][arrEnd[1]] = 2
    print("depois", arrEnd)
        
def moverPopulacao(arrEnd,tipo):
    for i in arrEnd:
        decidirDireçãoGeral(i,tipo)

count = 0
while count < 100:
    moverPopulacao(coordenadasPredadores,"predador")
    moverPopulacao(coordenadasPresas,"presa")
    checaColisao()
    cmapmine = ListedColormap(['w','b','r'], N=3)
    plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=2)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("ResultadoImagens/matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("ResultadoImagens/matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    count += 1
    

    
    
OS.system("cd ResultadoImagens/ && convert *.png ibs.gif && rm -rf *.png")


