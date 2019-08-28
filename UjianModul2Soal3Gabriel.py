from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, abort, url_for
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pokemon.html')

@app.route('/hasil', methods=['GET', 'POST'])
def cari():
    if request.method=='POST':
        formdata = json.dumps(request.form)
        formdata2 = json.loads(formdata)
        url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(formdata2["search"].lower())
        pokedata = requests.get(url) 
        return render_template('hasilpokemon.html',
                name = formdata2["search"],
                _id = pokedata.json()["id"],
                sprite = pokedata.json()["sprites"]["front_default"],
                height = pokedata.json()["height"],
                weight = pokedata.json()["weight"])

@app.errorhandler(Exception)
def notFound(error):
    return render_template('pokemonerror.html')
if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port=5000  
    )