from decouple import config
import requests


API_KEY = config('API_KEY')
url = 'https://api.themoviedb.org/3/'

class MovieAPI:

    def __init__(self, movie):
        self.movie = movie

    def search_movie(movie):
        movie_endpoint = f'search/movie?api_key={API_KEY}&query={movie}&language=pt-BR'
        search_path = url + movie_endpoint

        search = requests.get(search_path).json()
        results = search.get('results')

        if results == None:
            results = {}

        movies = {}
        movie_collection = []


        for item in results:
            
            movies = {
                "movie_id" : item.get('id'),
                "movie_name" : item.get('original_title'),
                "overview" : item.get('overview')
            }

            if movies['overview'] == '':
                movies['overview'] = 'Não encontrada. (404)'

            if not item.get('release_date'):
                movies["release_date"] = '???'

            if item.get('release_date'):
                movies["release_date"] = item.get('release_date')[:4]

            if item.get('poster_path'):
                movies["movie_image"] = 'https://image.tmdb.org/t/p/original' + item.get('poster_path')

            movie_collection.append(movies)

        return movie_collection
    
    # I couldn't find a way to translate the movies' titles to Portuguese (tmdb API alternative titles isn't enough).
    # Não consegui encontrar uma maneira de traduzir os nomes dos filmes para Português (a API do tmdb não é suficiente).

    # I will let the function commented.
    # Vou deixar a função comentada.

    # def search_alternative_title(id):
    #     alt_titles_endpoint = f'movie/{id}/alternative_titles?api_key={API_KEY}'
    #     search_path = url + alt_titles_endpoint

    #     search = requests.get(search_path).json()
    #     alt_titles = search.get('titles')
    #     return alt_titles