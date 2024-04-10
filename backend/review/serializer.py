from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from review.models import FilmReview

class FilmReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmReview
        fields = '__all__'

    def validate_rate(self, obj):
        if obj < 0 or obj > 5:
            raise ValidationError("The rate value must to be between 0 and 5.")
        return obj