from rest_framework import serializers
from . import models


class DirectorSerializers(serializers.ModelSerializer):
    counts = serializers.SerializerMethodField()
    class Meta:
        model = models.Director
        fields = "all"

        def get_director_count(self, obj):
            return obj.counts.count()


class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "all"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "all"


class MovieSerializersList(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = "id title director reviews  filtered_reviews".split()


    def get_filtered_reviews(self, product):
        reviews = product.reviews.filter(stars__gt=2)

        return [{'id': review.id,
                 'text': review.text,
                 'reviews': review.stars} for review in reviews]