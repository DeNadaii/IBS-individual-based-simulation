import matplotlib.pyplot as plt
import random
import math

pi = math.pi
e = math.e

Range = 0.5
arrPontos = [1,6]
Resultado_Paux = []
Resultado_Fdp = []

def Xtil(Xzero, Xfinal, X):                                     #Xtil ta em função de x
    return Xzero + (((X)*(Xfinal - Xzero)))                     #X nesse caso é 0.3, mas sempre sera aleatorio
                                                         

def FDP(Xtil,Xzero):                                                                                          
    return (1/(math.sqrt(2*pi)))*(e**(0.5*((Xtil/Xzero)**2)))                #essa FDP é um exemplo; FDP em funçao de Xtil                                   #return Xzero-(Xzero*((1-Xtil)**2))
    


while True:
    alpha = random.uniform(0.0, 2.0)
    beta  = random.uniform(0.0, 2.0)
    
    Xzero  = arrPontos[0]
    Xfinal = Xzero + Range
    print("xzero1", Xzero)
    
    Paux = alpha                                            #Probabilidade auxiliar
    X = beta                                                #variavel independente (extocastica)
    ResultadoFDP = FDP(Xtil(Xzero,Xfinal, X),arrPontos[0])
    
    if Paux <= ResultadoFDP:
        print("bom sorteio")
        Resultado_Paux.append(Paux)
        Resultado_Fdp.append(ResultadoFDP)    
        arrPontos[0] = Xfinal
        print("xzero2", Xzero)
    
    if Xfinal == arrPontos[1]:
        break
    
print(Resultado_Fdp)
print(Resultado_Paux)

produtos = ["produto a","produto b","produto c","produto d","produto e",]
numero = [1,2,3,4,5]

plt.plot(Resultado_Paux,Resultado_Fdp)
plt.show()