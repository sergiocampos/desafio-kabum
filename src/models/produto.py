from flask_restplus import field
from src.server.instance import server

produto = server.api.model('Produto', {
    'dimensao': field.int(description='Altura'),
    'peso': field.int(description='peso')
})