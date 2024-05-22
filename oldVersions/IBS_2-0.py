import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os as OS

class Predador:
    def __init__(self, genero, idade, posicao):
        self.genero = genero
        self.idade = idade
        self.posicao = posicao
        
    def apresentar(self):
        print("genero: ", self.genero, "\nidade: ", self.idade, "\nposicao: ", self.posicao)

    def crescimentoPredador(self):
        if self.idade < 4:
            self.idade += 1
    def getEndereco(self):
        return self.posicao
    def getGenero(self):
        return self.genero
    def getIdade(self):
        return self.idade
        
L = 50

matrix = np.zeros((L, L))

Predadores = []

def gerarPresa():
    presa_x = np.random.randint(0,L-1)
    presa_y = np.random.randint(0,L-1)
    matrix[presa_x][presa_y] = 2
    
def gerarPredador():
    IdadePredador = np.random.randint(0,4)
    predador_x = np.random.randint(0,L-1)
    predador_y = np.random.randint(0,L-1)
    matrix[predador_x][predador_y] = 1
    Predadores.append(Predador("M",IdadePredador,[predador_x,predador_y]))

def popularMatriz():
    i = 0
    while i < 10:    
        gerarPredador() 
        i += 1
    i = 0
    while i <= 4:
        gerarPresa()
        i += 1


print("Predadores: ", Predadores)
popularMatriz()

def gerarLarva(endPredador):
    print("enderaco da larva", endPredador)
    matrix[endPredador[0],endPredador[1]] = 2
    Predadores.append(Predador("M",1,[endPredador[0],endPredador[1]]))
    
        

def decidirDireçãoGeral(arrEnd):
        n = np.random.randint(0,2) 
        p = np.random.randint(0,2)
        matrix[arrEnd[0]][arrEnd[1]] = 0
        if p == 0:
            delta = (-1)**n
            arrEnd[1] += delta
            print("fora da borda pela pra cima ou pra baixo")
            if arrEnd[1] > (L-1):
                arrEnd[1] = 0
                print("depois EIXO Y", arrEnd)
            if arrEnd[1] < 0:
                arrEnd[1] = (L-1)
                print("depois EIXO Y", arrEnd)
            matrix[arrEnd[0]][arrEnd[1]] = 1
        else:
            delta = (-1)**n
            arrEnd[0] += delta
            print("fora da borda pelo esquerda ou direita")
            if arrEnd[0] > (L-1):
                arrEnd[0] = 0
                print("depois EIXO X", arrEnd)
            if arrEnd[0] < 0:
                arrEnd[0] = (L-1)
                print("depois EIXO X", arrEnd)
            matrix[arrEnd[0]][arrEnd[1]] = 1
        
def moverPopulacao(ObjetoPredador):
    for i in ObjetoPredador:
        if i.getIdade() > 1:
            decidirDireçãoGeral(i.getEndereco())
        i.crescimentoPredador()
        
for i in Predadores:
    print(i.getEndereco())
        
count = 0
while count < 50:
    moverPopulacao(Predadores)
    cmapmine = ListedColormap(['w','b','r'], N=3)
    plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=2)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("ResultadoImagens/matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("ResultadoImagens/matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    print("count",count)
    count += 1

print(matrix)
    
OS.system("cd ResultadoImagens/ && convert *.png ibs.gif && rm -rf *.png")


