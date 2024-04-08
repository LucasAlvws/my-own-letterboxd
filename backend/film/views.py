from django.shortcuts import get_object_or_404

from rest_framework import mixins
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from film.models import Film
from film.serializer import FilmSerializer


class FilmRetrieveAPIView(RetrieveAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    lookup_field = "pk"


class FilmListCreateAPIView(ListCreateAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()


class FilmUpdateAPIView(UpdateAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    lookup_field = "pk"


class FilmDestroyAPIView(DestroyAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    lookup_field = "pk"


class FilmViewSetAPIView(
    GenericAPIView,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    lookup_field = "pk"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


@api_view(["GET", "POST", "PUT", "DELETE"])
def film_api_view(request, pk=None, *args, **kwargs):
    if request.method == "POST":
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == "GET":
        if pk:
            obj = get_object_or_404(Film, pk=pk)
            data = FilmSerializer(obj).data
            return Response(data)
        queryset = Film.objects.all()
        data = FilmSerializer(queryset, many=True).data
        return Response(data)
