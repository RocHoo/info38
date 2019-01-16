from flask import Flask,session

from flask_session import Session

from redis import StrictRedis

from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand

from config import Config

app=Flask(__name__)


app.config.from_object(Config)

Session(app)

manage=Manager(app)

db=SQLAlchemy(app)

Migrate(app,db)

manage.add_command('db',MigrateCommand)

@app.route('/')
def index():
    session['itcast']='2019'
    return 'hello world'

if __name__ == '__main__':
    manage.run()