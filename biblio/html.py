debuthtml='const/debuthtml.txt'
finhtml='const/finhtml.txt'
deb='<tr>'
fin='</tr>'
data_deb='<td>'
data_fin='</td>'

colors = ['#FFFFFF','#FA5858','#FA8258','#FAAC58','#F7D358','#F4FA58','#D0FA58','#82FA58']
"""
renvoie la couleur dans une case td d'une ligne tr d'une table
"""
def couleur(indice=1):
    """
    le nombre est coloré sur fond blanc
    """
    reponse=f'<font color="{colors[indice]}"> {indice} </font> '
    return reponse

def couleur2(indice=1):
    """
    le nombre est noir sur fond coloré.
    """
    reponse=f'<td bgcolor="{colors[indice]}"> <font> {indice} </font> '
    return reponse

"""
renvoie l'entete d'une page html
"""
def EnteteHtml(fichier=debuthtml):
    with open(fichier) as f :
        entete = f.read()
    return entete
"""
renvoie le pied d'une page html
"""
def PiedHtml(fichier=finhtml):   
    with open(finhtml) as f :
        pied = f.read()
    return pied