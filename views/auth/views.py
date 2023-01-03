from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ...database.database import db
from ...database.database import User
from flask_login import login_user

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')


        if not username:
            error = 'É necessário um nome de usuário.'
            flash(error)

        if not password:
            error = 'É necessário uma senha.'
            flash(error)

        try:

            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.login'))

        except Exception as req_error:
            print(req_error)

    return render_template('register.html')


@auth.route('/login', methods=["GET", "POST"])
def login():

    if request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')

        try:

            user = User.query.filter_by(username=username).first()

            if user is None:
                error = 'Credenciais inválidas ou incorretas.😑'
                flash(error)
            
            elif not check_password_hash(user.password, password):
                error = 'Credenciais inválidas ou incorretas.😑'
                flash(error)

            elif username == user.username and check_password_hash(user.password, password):
                login_user(user, remember=False)
                return redirect(url_for('user.user_home'))


        except Exception as req_error:
            print(req_error)

    return render_template('login.html')


