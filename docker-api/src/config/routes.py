from flask import Blueprint
from flask_restplus import Api
from src.controllers.user import UserController, UserUpdateController

blueprint_urls = Blueprint('url_global', __name__)
api = Api(blueprint_urls, prefix='/api')

api.add_resource(UserController, '/user')
api.add_resource(UserUpdateController, '/user/<string:id>')