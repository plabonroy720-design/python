import numpy as np
data=[]
p=int(input("Enter the number of the pages : "))
r=int(input("Enter the number of the row : "))
for i in range(p):
    block=[]
    print(f'Enter the information of the block {i+1}')
    for j in range(r):
        rows=list(map(int, input("Enter the numbers of the students : ").split()))
        block.append(rows)
    data.append(block)
a=np.array(data)
print(a)
print("")
b=a.T

print(a.shape)
print(b.shape)
