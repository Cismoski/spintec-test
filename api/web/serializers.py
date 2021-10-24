from rest_framework import serializers

from web import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = models.News
        fields = '__all__'
