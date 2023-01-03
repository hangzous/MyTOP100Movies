from flask import Flask, render_template, make_response
from decouple import config
from .database import database
from .views.auth.views import auth
from .views.users.views import user
from .views.generic.views import generic
from .utils import flask_login

app = Flask(__name__)

app.config['SECRET_KEY'] = config('SECRET_KEY')


DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_NAME = config('DB_NAME')

flask_login.init(app)


app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'

database.init(app)

app.register_blueprint(user)
app.register_blueprint(auth)
app.register_blueprint(generic)

@app.errorhandler(404)
def page_not_found(error):
    return make_response(render_template('error_404.html'), 404)