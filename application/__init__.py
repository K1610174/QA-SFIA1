from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from application import routes
