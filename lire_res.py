from constantes.html import deb,fin, couleur,data_fin,data_deb
from constantes.html import EnteteHtml,PiedHtml,couleur2

Fichier='resultats-7.txt'

"""
Récupère les entete et pied d'une page html
"""
entete = EnteteHtml()
pied = PiedHtml()
"""
fichier de sortie au format html
"""
fhtml = open("matrice.html","w")
"""
l'entete sera celui du modèle
"""
fhtml.write(entete)

"""
lecture des données créées par matrix.py
"""
with open(Fichier) as file :
    info = file.read().splitlines()


i=1
for ligne in info :
    if ( i < 8 ) :
        fhtml.write(deb)
        line=ligne.split(' ')
        if i > 1 : line.pop(0)
        codehtml=''
        for elt in line :
            val=int(elt)
            codehtml = codehtml + couleur2(val) + data_fin
        fhtml.write(codehtml)
        fhtml.write(fin)
        fhtml.write('\n')
    i=i+1


fhtml.write(pied)
fhtml.close()