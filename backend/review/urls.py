from django.urls import path

from review.views import (
    FilmReviewRetriveAPIView,
    FilmReviewListCreateAPIView,
    FilmReviewDestroyAPIView,
    FilmReviewUpdateAPIView,
    FilmReviewGenericViewSetAPIView
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('viewset', FilmReviewGenericViewSetAPIView, basename="review")

urlpatterns = router.urls
urlpatterns += [
    path(
        "classview/<int:pk>/",
        FilmReviewRetriveAPIView.as_view(),
        name="classview_retrive_review",
    ),
    path(
        "classview/<int:pk>/update/",
        FilmReviewUpdateAPIView.as_view(),
        name="classview_retrive_review",
    ),
    path(
        "classview/<int:pk>/delete/",
        FilmReviewDestroyAPIView.as_view(),
        name="classview_retrive_review",
    ),
    path(
        "classview/",
        FilmReviewListCreateAPIView.as_view(),
        name="classview_list_review",
    ),
]
