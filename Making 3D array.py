import numpy as np
data=[]
block=int(input("Enter the numbers of the blocks : "))
row=int(input("Enter the numbers of the rows : "))
for i in range(block):
    blocks=[]
    print(f"Enter the imformation in the block {i+1}")
    for j in range(row):
        rows=list(map(int,input(f"Enter the marks of the student {j+1} : ").split()))
        blocks.append(rows)
    data.append(blocks)
a=np.array(data)
print(a)
