import numpy as np
a=[]
c=int(input("Enter  how many students : "))
for i in range(c):
    row=list(map(int, input(f"Student {i+1} marks : ").split()))
    a.append(row)
b=np.array(a)
print(b)
