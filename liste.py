import random 
from flask import Flask, render_template

"""
création de données bidon


"""


# colors = ['#FFFFFF','#FA5858','#FA8258','#FAAC58','#F7D358','#F4FA58','#D0FA58','#82FA58']

colors = ['#FFFFFF','#FF0000','#FFFF00','#40FF00','#00FF40','#00BFFF','#4000FF','#DF013A']

def Creation_dico(N=3,M=7,modulo=7) :
    """
    test la valeur de modulo
    """
    if ( modulo <2 or modulo > 7) : modulo=7
    """
    creation d'un dictionnaire forme de N lignes et M colonnes
    """
    dico={}
    for i in range(0,N):
        ligne=[]
        for _ in range(0,M):
            """
            alimente la ligne par une liste de deux termes
            formé du nombre modulo 7 mais de 1 à 7
            et de la couleur associée 
            """
            val=(random.randint(1,M) % modulo) +1
            col=colors[val]
            ligne.append([val,col])
        """
        alimente le dico
        """
        dico[i]=ligne
    """
    affiche le dico
    """
    return dico

"""
partie flask

"""
app = Flask(__name__)
"""
bidon affiche un carré de 40 de coté

"""

@app.route('/bidon')
def bidon():
    dico = Creation_dico(40,40)

    return render_template('carre.html', result=dico)

"""
carre affiche un carré de côté paramétré

"""

@app.route('/carre/<int:cote>')
def carre(cote):
    dico = Creation_dico(cote,cote)

    return render_template('carre.html', result=dico)

"""
rectangle affiche un rectangle de dimension paramétré

"""

@app.route('/rectangle/<int:hauteur>/<int:largeur>/<int:modulo>')
def rectangle(hauteur,largeur,modulo):
    dico = Creation_dico(hauteur,largeur,modulo)

    return render_template('carre.html', result=dico)


if __name__ == '__main__':

    app.run(debug=True)