import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:9Aba-lqnb@localhost:3306/taskplaner'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hello12345@localhost:3306/taskplaner'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
