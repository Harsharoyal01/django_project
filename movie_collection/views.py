import os
import requests
import collections
from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections.models import Movie
from collections import Counter  # Correctly imported from collections

@api_view(['GET'])
def fetch_movies(request):
    username = os.getenv('API_USERNAME')
    password = os.getenv('API_PASSWORD')
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    movies = []

    while url:
        response = requests.get(url, auth=(username, password))

        if response.status_code == 200:
            data = response.json()
            for movie_data in data['data']:
                movie, created = Movie.objects.get_or_create(
                    uuid=movie_data['uuid'],
                    defaults={
                        'title': movie_data['title'],
                        'description': movie_data['description'],
                        'genres': movie_data['genres'],
                    }
                )
                movies.append({
                    'title': movie.title,
                    'description': movie.description,
                    'genres': movie.genres,
                    'uuid': str(movie.uuid)
                })
            url = data['next']  # Move to the next page if available
        else:
            return Response({'error': 'Unable to fetch movies'}, status=response.status_code)

    return Response({
        'count': len(movies),
        'next': None,
        'previous': None,
        'data': movies,
    })
