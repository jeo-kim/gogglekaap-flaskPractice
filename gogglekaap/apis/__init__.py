from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

api = Api(
    blueprint,
    title='Goggle kaap API',
    version='1.0',
    doc='/docs',
    description='Welcome my API docs'
)

#Todo : add namespace to Blueprint