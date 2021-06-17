from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app=Flask(__name__)

app.config['SECRET_KEY']='e5aeeed185224376330bc6b0a1b0de38'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

from flaskblog import routes
