from flask_restplus import field
from src.server.instance import server

transportadoras = server.api.model('Transportadora', {
    'id': field.String(description='Id'),
    'tittle': field.String(description='Nome da transportadora.'),
    'constante_calculo': field.String(description='Valor da constante de calculo.'),
    'altura_min': field.String(description='Altura Minima'),
    'altura_max': field.String(description='Altura Máxima'),
    'largura_min': field.String(description='Largura Minima'),
    'largura_max': field.String(description='largura maxima'),
    'prazo_entrega': field.String(description='Prazo de entrega'),
})