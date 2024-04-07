from rest_framework import serializers

from review.models import FilmReview

class FilmReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmReview
        fields = '__all__'
