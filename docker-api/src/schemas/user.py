from flask_marshmallow import Schema
from marshmallow import fields

class UserSchema(Schema):
    id = fields.String()
    class Meta:
        fields = ("id", "username", "password", "role")
        ordered = True

users_schema = UserSchema(many=True)
user_schema = UserSchema()