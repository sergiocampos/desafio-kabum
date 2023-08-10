from flask import Flask
from flask import jsonify
from flask_restx import Api
from flask_restx import Resource
import json

from src.server.instance import server
from src.server.models.produtos import produtos

app = server.app
api = server.api

@api.route('/produtos')
class Produto(Resource):
    
    def post(self, ):
        response = api.payload
        return response, 200 
