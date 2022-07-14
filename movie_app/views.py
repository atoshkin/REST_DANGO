from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status


@api_view(['GET'])
def DirectorListView(request):
    directors = models.Director.objects.all()
    data = serializers.DirectorSerializers(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def DirectorDetailView(request, id):
    try:
        director = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Director not found'})
    data = serializers.DirectorSerializers(director).data
    return Response(data=data)


@api_view(['GET'])
def MovieListView(request):
    movie = models.Movie.objects.all()
    data = serializers.MovieSerializersList(movie, many=True).data
    return Response(data=data)




@api_view(['GET'])
def MovieDetailView(request, id):
    try:
        movie = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found'})
    data = serializers.MovieSerializersDetail(movie).data
    return Response(data=data)





@api_view(['GET'])
def ReviewListView(request):
    review = models.Review.objects.all()
    data = serializers.ReviewSerializers(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def ReviewDetailView(request, id):
    try:
        review = models.Review.objects.get(id=id)
    except models.Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Peview not found'})
    data = serializers.ReviewSerializers(review).data
    return Response(data=data)
