

from http.client import responses
import os
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/', methods=["GET"])
def main():
    return render_template('calculadora.html')

@app.route('/resultado', methods=["POST"])
def resultado():
    numero1 = int(request.form['numero1'])
    numero2 = int(request.form['numero1'])
    conta = request.form['conta']
    contas = {
        'soma' : lambda x, y: x + y,
        'sub' : lambda x, y: x - y,
        'mult' : lambda x, y: x * y,
        'div' : lambda x, y: x / y
    }

    resultado = contas[conta](numero1, numero2)
    return render_template('resultado.html', resultado=resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)