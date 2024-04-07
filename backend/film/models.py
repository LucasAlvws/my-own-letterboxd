from django.db import models

# Create your models here.


FILM_TYPES = (
    ("horror", "Terror"),
    ("action", "Ação"),
    ("drama", "Drama"),
    ("comedy", "Comédia"),
    ("romance", "Romance"),
    ("fantasy", "Fantasy"),
    ("science_fiction", "Ficção Científica"),
)


class Film(models.Model):
    name = models.CharField(
        max_length=120, verbose_name="Nome", blank=False, null=False
    )
    director_name = models.CharField(
        max_length=120, verbose_name="Diretor", blank=False, null=False
    )
    duration = models.IntegerField(
        verbose_name="Duração (Min)", blank=False, null=False
    )
    description = models.TextField(verbose_name="Descrição", blank=False, null=False)
    film_type = models.CharField(
        max_length=80, choices=FILM_TYPES, blank=False, null=False
    )

    def __str__(self):
        return self.name
