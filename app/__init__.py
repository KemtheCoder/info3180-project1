from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = '/app/static/uploads'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password123@localhost/project1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'mydatabase.db')
app.debug = True
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
