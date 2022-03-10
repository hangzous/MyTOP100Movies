from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

# Aqui estão localizados todos os modelos para o banco de dados (tabelas e colunas)

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(35), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    movies = db.relationship('Movies', backref='user')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.password}')"


class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    list_name = db.Column(db.String(100), nullable=False)
    movie_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Movies('{self.list_name}', '{self.movie_name}')"