from flask import Blueprint, redirect, request, render_template, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.database import User
from flask_login import login_required, login_user, current_user, logout_user


accounts = Blueprint('accounts', __name__)


@accounts.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    error = None

    if current_user.is_authenticated:
        return redirect(url_for('user.user_home'))

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')


        if not username:

            error = 'É necessário um nome de usuário.'
            flash(error, category='error')

        if not password:

            error = 'É necessário uma senha.'
            flash(error, category='error')
        
        if error is None:

            try:

                user = User(username=username, password=generate_password_hash(password))
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('accounts.entrar'))

            except Exception as any_error:
                print(f'Houve um erro: {any_error}')


    return render_template('cadastro.html')


@accounts.route('/entrar', methods=['GET', 'POST'])
def entrar():
   
    error = None

    if current_user.is_authenticated:
        return redirect(url_for('user.user_home'))

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')


        user = User.query.filter_by(username=username).first()
        
        if user is None:

            error = 'Credenciais inválidas ou incorretas.'
            flash(error, category='error')

        elif not check_password_hash(user.password, password):

            error = 'Credenciais inválidas ou incorretas.'
            flash(error, category='error')

        elif username == user.username and check_password_hash(user.password, password):

            login_user(user, remember=True)
            return redirect(url_for('user.user_home'))


    return render_template('login.html')


@accounts.route('/sair')
@login_required
def sair():
    
    logout_user()
    return redirect(url_for('accounts.entrar'))