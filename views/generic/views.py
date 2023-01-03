from flask import Blueprint, request, render_template, make_response
from ...database.database import Movies, User, db
from sqlalchemy.sql import select


generic = Blueprint('generic' ,__name__)

@generic.route('/lists', methods=["GET"])
def search_lists():
    args = request.args
    search = args.get('search')

    if search == None:
        search = ''

    statement = select([User.username, Movies.list_name, Movies.movie_name]).\
        filter(Movies.list_name.op('~*')(f"{search}")).\
        where(Movies.user_id==User.id)

    lists = db.session.execute(statement).fetchall()

    return render_template('generic/search_lists.html', search=search, lists=lists)


@generic.route('/profile/<username>', methods=["GET"])
def view_public_user_profile(username):

    user_statement = select([User]).where(User.username==username)
    result = db.session.execute(user_statement).first()
    
    if result == None:
        return make_response(render_template('error_404.html'), 404)

    user = result[0]

    lists_statements = select([Movies.list_name, Movies.movie_name]).where(Movies.user_id==user.id)
    result = db.session.execute(lists_statements).fetchall()

    return render_template('generic/public_user_profile.html', username=user.username, lists=result)
