from src.models.user import User
from src.schemas.user import users_schema, user_schema
import json

class UserService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def fetch(self):
        try:
            users = User.objects()
        except:
            return None
        return users_schema.dump(users)
    
    def create(self, **body):
        try:
            created_user = User(**body).save()
        except:
            return None
        return user_schema.dump(created_user)
    
    def retrieve(self, id):
        try:
            user = User.objects.get(id = id)
        except:
            return None
        return user_schema.dump(user)
    
    def modify(self, id, **body):
        try:
            updated_user = User.objects.get(id=id).update(**body)
            new_user_data = User.objects.get(id=id)
        except:
            return None
        return user_schema.dump(new_user_data)
        
    def delete(self, id):
        try:
            deleted_user  = User.objects.get(id=id).delete()
        except:
            return None
        return  'Usuario Eliminado'
