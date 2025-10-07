from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer

def home(request):
    return HttpResponse("<h1>🎬 Welcome to the Movie API Project!</h1><p>Use /admin to manage movies or /movies/ to view movie data.</p>")

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
