import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import os as OS


L = 20

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
    while i < 10:    
        gerarPresa()   
        gerarPredador() 
        i += 1


popularMatriz()

def decidirDireçãoGeral(arrEnd):
    n = np.random.randint(0,2) 
    p = np.random.randint(0,2)
    print("p: ", p)
    print("n: ", n)
    if p == 0:
        delta = (-1)**n
        arrEnd[1] += delta
    else:
        delta = (-1)**n
        arrEnd[0] += delta
        

count = 0
while count < 10:
    print("count: ", count)
    print("BEFORE: ", coordenadasPredadores[count])
    decidirDireçãoGeral(coordenadasPredadores[count])
    print("AFTER: ",coordenadasPredadores[count])
    count += 1