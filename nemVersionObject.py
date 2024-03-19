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
    
    

L = 10


matrix = np.zeros((L, L))

Predadores = []

def gerarPresa():
    presa_x = np.random.randint(2,L-2)
    presa_y = np.random.randint(2,L-2)
    matrix[presa_x][presa_y] = 1
    matrix[presa_x][presa_y+1] = 1
    matrix[presa_x+1][presa_y] = 1
    matrix[presa_x+1][presa_y+1] = 1  
    
def gerarPredador():
    predador_x = np.random.randint(0,L-1)
    predador_y = np.random.randint(0,L-1)
    matrix[predador_x][predador_y] = 2
    Predadores.append(Predador("M",4,[predador_x,predador_y]))

def popularMatriz():
    i = 0
    while i < 5:    
        gerarPredador() 
        i += 1
    i = 0
    while i <= 1:
        gerarPresa()
        i += 1


print("Predadores: ", Predadores)
popularMatriz()

def gerarLarva(endPredador):
    print("enderaco da larva", endPredador)
    matrix[endPredador[0],endPredador[1]] = 2
    Predadores.append(Predador("M",1,[endPredador[0],endPredador[1]]))
    
        

def decidirDireçãoGeral(arrEnd, idade):
    n = np.random.randint(0,2) 
    p = np.random.randint(0,2)
    
    if matrix[arrEnd[0]][arrEnd[1]] == 1:
        gerarLarva(arrEnd)
        
    if idade == 4:
        print("pode se mover")
        matrix[arrEnd[0]][arrEnd[1]] = 0
        if p == 0:
            delta = (-1)**n    
            arrEnd[1] += delta
            if arrEnd[1] < 0 or arrEnd[1] > (L-1):
                #print("fora da borda pela pra cima ou pra baixo")
                if arrEnd[1] > (L-1):
                    arrEnd[1] = 0
                    #print("depois EIXO Y", arrEnd)
                if arrEnd[1] < 0:
                    arrEnd[1] = (L-1)
                    #print("depois EIXO Y", arrEnd)
            matrix[arrEnd[0]][arrEnd[1]] = 2
        else:
            delta = (-1)**n
            arrEnd[0] += delta
            if arrEnd[0] < 0 or arrEnd[0] > (L-1):
                #print("fora da borda pelo esquerda ou direita")
                if arrEnd[0] > (L-1):
                    arrEnd[0] = 0
                    #print("depois EIXO X", arrEnd)
                if arrEnd[0] < 0:
                    arrEnd[0] = (L-1)
                    #print("depois EIXO X", arrEnd)
            matrix[arrEnd[0]][arrEnd[1]] = 2
    else:
        print("nao pode se mover idade baixa")
        print(arrEnd)
        
def moverPopulacao(ObjetoPredador):
    for i in ObjetoPredador:
        decidirDireçãoGeral(i.getEndereco(),i.getIdade())
        
for i in Predadores:
    print(i.getEndereco())
        
count = 0
while count < 20:
    moverPopulacao(Predadores)
    cmapmine = ListedColormap(['w','b','r','g'], N=4)
    plt.matshow(matrix, cmap=cmapmine, vmin=0, vmax=3)
    plt.title("Frame {}".format(count))
    if count > 9:
        plt.savefig("ResultadoImagens/matrix_IBS_{}.png".format(count), bbox_inches='tight')
    else:
        plt.savefig("ResultadoImagens/matrix_IBS_0{}.png".format(count), bbox_inches='tight')
    print("count",count)
    count += 1

# for i in Predadores:
#     print("idade", i.getIdade())

print(matrix)
    
#OS.system("cd ResultadoImagens/ && convert *.png ibs.gif && rm -rf *.png")


