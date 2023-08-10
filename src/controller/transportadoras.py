from flask import Flask
from flask import jsonify
from flask_restx import Api
from flask_restx import Resource
import json

from src.server.instance import server
from src.models.produto import produto

app = server.app
api = server.api

transportadoras_db = [
    {'id': 1, 'title': 'Entrega Ninja', 'constante_calculo': 0.3, 'altura_min': 10, 'altura_max': 200, 'largura_min': 6, 'largura_max': 140, 'prazo_entrega': '6 dias'},
    {'id': 2, 'title': 'Entrega KaBuM', 'constante_calculo': 0.2, 'altura_min': 5, 'altura_max': 140, 'largura_min': 13, 'largura_max': 125, 'prazo_entrega': '4 dias'}
]

@api.route('/transportadoras')
class Transportadoras(Resource):
    
    def get(self, ):
        data_trans = jsonify({'transportadoras_db': transportadoras_db})
        with open("transportadoras.json") as file:
            data = json.load(file)
            print(data["transportadoras_db"][1]["largura_max"])
        return data_trans
    
    @api.expect(produto, validate=True)
    @api.marshal_with(produto)
    def post(self, ):
        response = api.payload
        transportadoras_db.append(response)
        return response, 200
