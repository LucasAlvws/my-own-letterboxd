from django.urls import path, include

urlpatterns = [
    path('film/', include("film.urls")),
    path('review/', include("review.urls")),
]
