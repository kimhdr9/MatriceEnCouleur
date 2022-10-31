def matriceU(N,val) :
    """
    ligne de zeros
    """
    zeros=[]
    for _ in range(0,N):
        zeros.append(val)

    """
    initialisation de la matrice
    """
    matrice=[]

    for _ in range(0,N):
        matrice.append(zeros)

    return matrice

# test de 
if __name__ == '__main__':
    """
    affichage
    """
    N=3
    matrice=matriceU(N,1)
    for i in range(0,N):
        print(matrice[i])
