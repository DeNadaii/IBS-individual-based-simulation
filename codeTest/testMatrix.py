import numpy as np

arrTest = [[0,0],[1,1],[2,2]]
arrEnd = [1,1]

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
    print("BEFORE: ", arrEnd)
    decidirDireçãoGeral(arrEnd)
    print("AFTER: ",arrEnd)
    count += 1
    