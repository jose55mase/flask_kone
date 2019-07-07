from flask import Flask, jsonify, render_template, request
import requests
import json
import unicodedata
app = Flask(__name__)


@app.route("/inicio")
def server_info():
    return render_template('Inicio.html')

@app.route("/", methods = ['POST', 'GET'])
@app.route("/sesion", methods = ['POST', 'GET'])
def login():
    info = requests.get('http://localhost:8000/login')
    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    info = json.loads(info)

    form = request.form
    if request.method == 'POST':
        for value in info:
            if form['usuario'] == str(info[value]):
                return render_template("Adentro.html", info=info)           
               
    return render_template("Sesion.html")
    
@app.route("/usuarios")
def adentro():
    return render_template("Usuarios.html")

@app.route("/adentro")
def Iniciado():
    return render_template("Adentro.html")

if __name__ == "__main__":
    app.run(port=7000, host="0.0.0.0", debug=True)