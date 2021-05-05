from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        #fields = ['id', 'title', 'author', 'email'] #or also can use
        fields = '__all__'