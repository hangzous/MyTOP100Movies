from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Você deve entrar em sua conta para acessar esta página.'

def init(app):
    login_manager.init_app(app)