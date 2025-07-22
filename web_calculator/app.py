import sys
import os
from flask import Flask, request, jsonify

# Adicionar o diretório pai ao sys.path para importar calculator_full
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import calculator_full as calc

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    result = calc.adicionar(a, b)
    return jsonify({'result': result})

@app.route('/api/subtract', methods=['POST'])
def subtract():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    result = calc.subtrair(a, b)
    return jsonify({'result': result})

@app.route('/api/multiply', methods=['POST'])
def multiply():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    result = calc.multiplicar(a, b)
    return jsonify({'result': result})

@app.route('/api/divide', methods=['POST'])
def divide():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    try:
        result = calc.dividir(a, b)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# Additional endpoints for scientific and statistical functions can be added similarly

if __name__ == '__main__':
    app.run(debug=True)
