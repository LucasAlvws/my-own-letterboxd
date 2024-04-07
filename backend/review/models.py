from django.db import models
from django.conf import settings

from film.models import Film

User = settings.AUTH_USER_MODEL

class FilmReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    like = models.BooleanField(default=False)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
