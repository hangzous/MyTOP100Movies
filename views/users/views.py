from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_required, logout_user
from ...utils.api import MovieAPI
from ...database.database import db, Movies, User
from werkzeug.security import generate_password_hash
from sqlalchemy import delete


user = Blueprint('user', __name__)


@user.route('/', methods=["GET"])
def user_home():

    if not current_user.is_authenticated:
        return render_template('/generic/site_home.html')

    user_lists = Movies.query.filter_by(user_id=current_user.id).all()

    return render_template('/users/user_home.html', lists=user_lists)


@user.route('/list/create-list', methods=["GET", "POST"])
@login_required
def create_list():

    args = request.args
    first_movie = args.get('first_movie', type=str)

    if first_movie == None:
        first_movie = ''

    api = MovieAPI
    movie_list = api.search_movie(first_movie)

    if request.method == 'POST':

        list_name = request.form.get('list_name')
        movie_name = request.form.get('movie_name')

        create = Movies(user_id=current_user.id, list_name=list_name, movie_name=movie_name)
        db.session.add(create)
        db.session.commit()

        return redirect(url_for('user.user_home'))

    return render_template('/users/create_list.html', movies=movie_list, first_movie=first_movie)


# Referente a página de configurações e suas ramificações 

@user.route('/settings', methods=["GET", "POST"])
@login_required
def settings():

    lists = Movies.query.filter_by(user_id=current_user.id).all()
    
    list_name = []

    for l in lists:
        list_name.append(l.list_name)

    return render_template('/users/settings.html', lists=list_name)


@user.route('/settings/change/username', methods=["POST"])
@login_required
def change_username():

    if request.method == 'POST':
        new_username = request.form.get('new_username')
        modified = User.query.filter(User.username == current_user.username).first()

        modified.username = new_username
        db.session.commit()

        return redirect(url_for('user.user_home'))


@user.route('/settings/change/password', methods=["POST"])
@login_required
def change_password():

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        modified = User.query.filter(User.password == current_user.password).first()

        modified.password = generate_password_hash(new_password)
        db.session.commit()

        return redirect(url_for('user.user_home'))

@user.route('/settings/delete/list', methods=["POST"])
@login_required
def delete_list():

    if request.method == 'POST':
        list_name = request.form.get('list')
        list_to_be_removed = Movies.query.filter(Movies.list_name==list_name).first()
        db.session.delete(list_to_be_removed)
        db.session.commit()

        return redirect(url_for('user.user_home'))


@user.route('/settings/delete/account', methods=["POST"])
@login_required
def delete_account():

    if request.method == 'POST':

        delete_all_movies = delete(Movies).where(Movies.user_id==current_user.id)
        delete_user = delete(User).where(User.username==current_user.username)

        db.session.execute(delete_all_movies)
        db.session.execute(delete_user)
        db.session.commit()

        logout_user()
        return redirect('/')

# Fim da parte de configurações


@user.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect('/')

