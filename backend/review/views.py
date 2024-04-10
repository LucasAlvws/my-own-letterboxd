from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


from review.models import FilmReview
from review.serializer import FilmReviewSerializer


class FilmReviewRetriveAPIView(generics.RetrieveAPIView):
    serializer_class = FilmReviewSerializer
    queryset = FilmReview.objects.all()
    lookup_field = "pk"


class FilmReviewListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FilmReviewSerializer
    queryset = FilmReview.objects.all()


class FilmReviewUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FilmReviewSerializer
    queryset = FilmReview.objects.all()
    lookup_field = "pk"


class FilmReviewDestroyAPIView(generics.DestroyAPIView):
    serializer_class = FilmReviewSerializer
    queryset = FilmReview.objects.all()
    lookup_field = "pk"


class FilmReviewGenericViewSetAPIView(ModelViewSet):
    serializer_class = FilmReviewSerializer
    queryset = FilmReview.objects.all()
    lookup_field = "pk"
