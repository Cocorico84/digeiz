from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
ma = Marshmallow(app)
