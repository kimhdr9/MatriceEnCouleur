def matricezero(N) :
    """
    ligne de zeros
    """
    zeros=[]
    for _ in range(0,N):
        zeros.append(0)

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
    matrice=matricezero(N)
    for i in range(0,N):
        print(matrice[i])
