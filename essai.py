from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tableau')
def tableau():
    dico ={
        'tomate' :3.99,
        'poulet' :15.99,
        'pommes' :2.99
    }

    return render_template('tableau.html', result=dico)

if __name__ == '__main__':
    app.run(debug=True)