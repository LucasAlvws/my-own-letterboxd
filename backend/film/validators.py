from rest_framework.validators import UniqueValidator

from film.models import Film

unique_film_name = UniqueValidator(queryset=Film.objects.all(), lookup='iexact')