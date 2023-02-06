from flask import Blueprint
from flask_restful import Api
from files.Register import Register
from files.Login import Login

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



api.add_resource(Register, '/register')
api.add_resource(Login, '/login')