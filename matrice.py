import random

"""
N longueur d'une ligne
"""
N=3

selection=[]


for i in range(1,N*N+1):
    selection.append(i)

mat=[]


for lig in range(0,N):
    ligne=[]
    for col in range(0,N):
        val=random.choice(selection)
        ligne.append(val)
        selection.remove(val)
    mat.append(ligne)

for i in range(0,N):
    print(mat[i])
