from rest_framework import viewsets, filters

from web import models, serializers


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ('author__name', 'title', 'body',)
