from flask_restplus import Resource
from flask import request
from src.services.user import UserService

class UserController(Resource):
    
    def __init__(self, *args, **kwargs):
        self.user_service = UserService()

    def get(self):
        users = self.user_service.fetch()
        if not users:
            return {'data': [], 'message': 'No se encontraron usuarios'}, 404
        return {'data': users, 'message': 'success'}, 200

    def post(self):
        body = request.get_json()

        data = self.user_service.create(**body)
        if not data:
            return {'message': 'Ocurrio un error al insertar'}, 404
        return {'data': data, 'message': 'Success'}, 200
    

class UserUpdateController(Resource):
    
    def __init__(self, *args, **kwargs):
        self.user_service = UserService()

    def get(self, id):
        users = self.user_service.retrieve(id)
        if not users:
            return {'data': [], 'message': 'No se encontró el usuario'}, 404
        return {'data': users, 'message': 'success'}, 200
    
    def put(self, id):
        body = request.get_json()
        
        data = self.user_service.modify(id, **body)
        if not data:
            return {'message': 'Ocurrio un error al modificar el usuario/Usuario no encontrado'}, 404
        return {'data': data, 'message': 'Success'}, 200
    
    def delete(self, id):
        data = self.user_service.delete(id)
        if not data:
            return {'message': 'Ocurrio un error al eliminar el usuario/Usuario no encontrado'}, 404
        return {'data': data, 'message': 'Success'}, 200