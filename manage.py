from flask import Flask,session

from flask_session import Session

from redis import StrictRedis

from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager

from flask_migrate import Migrate,MigrateCommand

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://roou:mysql@localhost/info_python38'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app.config['SECRET_KEY']='fE/S+iP1yeXBfEKRIL9mYCubw4AV6InrpByVbSPuz4L6MBANFL4DMg=='

app.config['SESSION_TYPE']='redis'

app.config['SESSION_REDIS']=StrictRedis(host='127.0.0.1',port=6379)

app.config['SESSION_USER_SINGER']=True

app.config['SESSION_PERMENENT_LIFETIME']=86400

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