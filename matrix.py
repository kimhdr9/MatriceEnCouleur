import numpy as np
import random

N=5
iterations=10000000

for _ in range(iterations):
    """
    ensemble des nombres entre 1 et N*N
    """
    selection=[]
    """
    alimente selection
    """
    for i in range(1,N*N+1): selection.append(i)

    matrix = np.zeros((N,N))


    for lig in range(0,N):
        for col in range(0,N):
            val=random.choice(selection)
            matrix[lig][col]=val
            selection.remove(val)
            
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