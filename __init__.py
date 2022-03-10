from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from decouple import config

"""
Esse arquivo será o responsável por reunir todos os módulos do projeto (Banco de Dados, API, etc...)
Consequentemente, sua função também será de iniciar o projeto como um todo, sendo por fim ativado pelo 
server.py
"""

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'accounts.entrar'
login_manager.login_message = 'Você deve entrar em sua conta para acessar está página.'

DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_NAME = config('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from .accounts.views import accounts
app.register_blueprint(accounts)


from .users.views import user
app.register_blueprint(user)
