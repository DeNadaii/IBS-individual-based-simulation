import random

x = [1,2,3,4,5]

for i in range(len(x)):
    for j in range(i + 1, len(x)): 
        print(i,j)
        
print(chr(random.randint(ord('M'), ord('F'))))

