from flask import Flask, jsonify, make_response, request
#IMPORTAR BANCO DE DADOS

from bd import Sensores
app = Flask('sensores')

#PASSO 1 - VISUALIZAR DADOS (GET)
@app.route('/sensores', methods = ['GET'])
def get_sensores():
    return Sensores

#PASSO 1.2 - VISUALIZAR OS DADOS POR ID (GET)
@app.route('/sensores/<int:id>', methods = ['GET'])
def get_sensores_id(id):
    for sensores in Sensores: 
        if sensores.get('id') == id:
            return jsonify(sensores)
        
#PASSO 2 - CRIAR NOVOS DADOS(POST)
@app.route('/sensores', methods=['POST'])
def criar_sensores():
    sensores = request.json
    Sensores.append(sensores)
    return make_response(
        jsonify(mensagem = 'Sensor cadastrado com sucesso', 
                sensores = sensores
                )

    )

#PASSO 3 - EDITAR DADOS (PUT)
@app.route('/sensores/<int:id>', methods = ['PUT'])
def editar_sensores_id(id):
    sensores_alterado = request.get_json()
    for indice, sensores in enumerate(Sensores):
        if sensores.get('id') == id:
            Sensores[indice].update(sensores_alterado)
            return jsonify(Sensores[indice])
        
#PASSO 4 - DELETAR DADOS (DELETE)
@app.route('/sensores/<int:id>', methods=['DELETE'])
def excluir_sensores(id):
    for indice, sensores in enumerate(Sensores):
        if sensores.get('id') == id:
            del Sensores[indice]
            return jsonify({'Mensagem:': 'Sensor excluido com sucesso!'})
        

app.run(port=5000, host='localhost')