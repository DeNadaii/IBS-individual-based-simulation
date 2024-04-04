import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random
import math

pi = math.pi
e = math.e

Range = 0.25
arrPontos = [-3,3]
Resultado_Xtil = []

def Xtil(Xzero, Xfinal, X):                                     #Xtil ta em função de x
    return Xzero + (((X)*(Xfinal - Xzero)))                     #X nesse caso é 0.3, mas sempre sera aleatorio
                                                         

def FDP(Xtil):                                                                                        
    return (1/(math.sqrt(2*pi)))*(e**(-(Xtil**2/(2*(arrPontos[0])**2))))                #essa FDP é um exemplo; FDP em funçao de Xtil                                   #return Xzero-(Xzero*((1-Xtil)**2))
    

count = 0
while count < 10000000:
    alpha = random.uniform(0.0, 1.0)
    beta  = random.uniform(0.0, 1.0)
    
    Paux = alpha                                            #Probabilidade auxiliar
    X = beta                                                #variavel independente (extocastica)
    
    ResultadoXtil = Xtil(arrPontos[0],arrPontos[1], X)
    ResultadoFDP = FDP(ResultadoXtil)
    
    if Paux <= ResultadoFDP:
        # print("bom sorteio")
        Resultado_Xtil.append(ResultadoXtil)
        count +=1 
        # print("xzero2", Xzero)
    print(count)
    


print("xtil",Resultado_Xtil)

plt.hist(Resultado_Xtil)
plt.show() 