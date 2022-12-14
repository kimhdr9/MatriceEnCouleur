import numpy as np
import random

N=10
M=N
iterations=10000000

for _ in range(iterations):
    
    matrix = np.zeros((N,N))


    for lig in range(0,N):
        ligne_ref=[]
        for i in range(1,M+1) : ligne_ref.append(i) 
        for col in range(0,N):
            val=random.choice(ligne_ref)
            matrix[lig][col]=val
            # print(lig,col,val)
            #  ne fonctionne que si M >= N
            ligne_ref.remove(val) 
            
    # print(matrix)
    # print(matrix.transpose())
    sumlig=[]
    for i in range(0,N): sumlig.append(0.)
    lig=1
    for a in matrix[:N,]:
        for e in a : sumlig[lig-1]=e+sumlig[lig-1]
        """
        affiche la somme
        """
        # print(f'Total des éléments pour ligne n° {lig} {a} : {sumlig[lig-1]}')
        lig=lig+1

    sumcol=[]
    for i in range(0,N): sumcol.append(0.)
    col=1
    for a in matrix[:,:N].transpose():
        for e in a :  sumcol[col-1]=e+sumcol[col-1]
        """
        affiche la somme
        """
        # print(f'Total des éléments pour colonne n° {col} {a} : {sumcol[col-1]}')
        col=col+1

    ok=True
    for i in range(1,N) :
        if sumlig[0] != sumlig[i] :
            ok=False
            break
        if sumcol[0] != sumcol[i] :
            ok=False
            break

    if ok :
        print(matrix)