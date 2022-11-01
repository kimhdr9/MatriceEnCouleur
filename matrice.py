import random

"""
N longueur d'une ligne
"""
N=3

for _ in range(100):
    """
    ensemble des nombres entre 1 et N*N
    """
    selection=[]
    """
    alimente selection
    """
    for i in range(1,N*N+1):
        selection.append(i)
    """
    crée une matrice vide
    """
    mat=[]
    """
    alimente de façon aléatoire à partir de l'ensemble "selection"
    """
    for lig in range(0,N):
        ligne=[]
        for col in range(0,N):
            val=random.choice(selection)
            ligne.append(val)
            selection.remove(val)
        mat.append(ligne)
    """
    somme les colonnes
    """
    somme=[]
    for _ in range(3) :
        somme.append(0)

    for i in range(0,N):
        somme[i]=0
        for elt in mat[i]:
            somme[i] = somme[i] + elt
    """
    si elles sont égales alors affiche la matrice
    """
    if somme[0]==somme[1] and somme[0]==somme[2] :
        for i in range(0,N):
            print(mat[i])

