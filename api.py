from decouple import config
import requests

API_KEY = config('API_KEY')
url = 'https://api.themoviedb.org/3/'

class QueryAPI:

    def __init__(self, movie):
        self.movie = movie

    def search_movie(movie):
        movie_endpoint = f'search/movie?api_key={API_KEY}&query={movie}'
        movie_path = url + movie_endpoint

        search = requests.get(movie_path).json()
        results = search.get('results')

        movies = {}
        movie_collection = []

        for item in results:
            
            movies = {
                "movie_id" : item.get('id'),
                "movie_name" : item.get('original_title')
            }

            if item.get('release_date'):
                movies["release_date"] = item.get('release_date')[:4]

            if item.get('poster_path'):
                movies["movie_image"] = 'https://image.tmdb.org/t/p/original' + item.get('poster_path')

            movie_collection.append(movies)

        return movie_collection