from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.database import Movies
from app.api import QueryAPI

"""
Este blueprint é responsável por lidar com todos os processos relacionados ao usuário após ter efetuado o login.
As funções aqui presentes serão as responsáveis por relacionar os utilitários de criação, modificação e remoção de elementos da lista de filmes.
"""


user = Blueprint('user', __name__)


@user.route('/')
def user_home():
    if not current_user.is_authenticated:
        return render_template('site_home.html')
    else:
        user_records = Movies.query.filter_by(user_id=current_user.id).all()
        
        if user_records == []:
            list_name = None
            first_movie = None

        elif user_records[0].list_name and user_records[0].movie_name:
            list_name = user_records[0].list_name
            first_movie = user_records[0].movie_name

        return render_template('user_home.html', list_name=list_name, first_movie=first_movie)


@user.route('/criar', methods=['GET', 'POST'])
@login_required
def criar_lista():

    if request.method == 'POST':

        # Busca os filmes por meio da API
        
        movie_name = request.form.get('movie')

        api = QueryAPI
        movie_list = api.search_movie(movie_name)

        return render_template('filmes/criar_lista.html', movies=movie_list)


    if request.method == 'GET':

        user_records = Movies.query.filter_by(user_id=current_user.id).all()

        if user_records == []:    
            return render_template('filmes/criar_lista.html')
        
        elif user_records[0].list_name:
            return redirect(url_for('user.user_home'))

          

@user.route('/criar/lista', methods=['GET', 'POST'])
@login_required
def finalizar():

    if request.method == 'POST':
        
        list_name = request.form.get('list_name')
        movie_name = request.form.get('movie')

        try:
            
            add_first_movie = Movies(
                user_id=current_user.id,
                list_name=list_name,
                movie_name=movie_name
            )

            db.session.add(add_first_movie)
            db.session.commit()

            return redirect(url_for('user.user_home'))
            
        except Exception as any_error:

            print(f'Houve um erro: {any_error}')

    return redirect(url_for('user.user_home'))


@user.route('/adicionar')
@login_required
def adicionar_filme():
    return render_template('filmes/adicionar_filme.html')


@user.route('/modificar')
@login_required
def modificar_lista():
    return render_template('filmes/modificar_lista.html')


@user.route('/remover')
@login_required
def remover_filme():
    return render_template('filmes/remover_filme.html')