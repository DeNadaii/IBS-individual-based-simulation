import numpy as np

arrTest = [[-1,-1],[1,1],[3,3]]

endInArray = 0
for i in arrTest:
    if i[0] < 0 or i[0] > len(arrTest)-1:
        print(i[0])
        print("out of range")
    if i[1] < 0 or i[1] > len(arrTest[0])-1:
        print(i[1])
        print("out of range")