from django.urls import path

from film.views import (
    FilmListCreateAPIView,
    FilmRetrieveAPIView,
    FilmUpdateAPIView,
    FilmDestroyAPIView,
    film_api_view
)

urlpatterns = [
    path("funcview/", film_api_view, name="func_list_create_film"),
    path("funcview/<int:pk>/", film_api_view, name="func_retrive_film"),
    path("classview/", FilmListCreateAPIView.as_view(), name="class_list_create_film"),
    path("classview/<int:pk>/detail/", FilmRetrieveAPIView.as_view(), name="class_retrive_film"),
    path("classview/<int:pk>/update/", FilmUpdateAPIView.as_view(), name="class_update_film"),
    path("classview/<int:pk>/delete/", FilmDestroyAPIView.as_view(), name="class_delete_film"),
]
