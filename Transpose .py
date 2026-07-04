import numpy as np
data=[]
a=int(input("Enter the numbers of the rows : "))
for i in range(a):
    b=list(map(int, input("Enter the numbers of the students : ").split()))
    data.append(b)
s=np.array(data)
print("Before the transpose of the array ........")
print(s)
print("")
print("After the transpose of the array ............")
print(s.T)
