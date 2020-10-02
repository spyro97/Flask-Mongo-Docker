from flask import Flask
import os
from src.config.routes import blueprint_urls
from src.config.db import initialize_db
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

#app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
}

initialize_db(app)

app.register_blueprint(blueprint_urls)