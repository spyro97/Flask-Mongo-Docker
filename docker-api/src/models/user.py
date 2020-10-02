from src.config.db import db
import mongoengine_goodjson as gj

class User(gj.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    role = db.StringField(required=True)