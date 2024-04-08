from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from film import validators
from film.models import Film


class FilmSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validators.unique_film_name])

    class Meta:
        model = Film
        fields = ["id", "name", "director_name", "duration", "description", "film_type"]

    def validate_duration(self, obj):
        if obj < 0:
            raise ValidationError("Durantion can not be less than 0 (zero).")
        elif obj > 500:
            raise ValidationError("Durantion can not be that long.")
        return obj