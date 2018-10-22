from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

api = Api(app)
db = SQLAlchemy(app)

v1 = api.namespace('v1', 'Version 1')
