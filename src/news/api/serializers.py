from news.models import *
from rest_framework.serializers import ModelSerializer,SerializerMethodField

from django.contrib.auth import get_user_model
User = get_user_model()


class AuthorSerializer(ModelSerializer):
	class Meta:
		model = Author
		fields = [
			'name'

		]

class CategorySerializer(ModelSerializer):
	class Meta:
		model = Category
		fields = [
			'name'
		]

class ArticleSerializer(ModelSerializer):
	authors = AuthorSerializer(many=True)
	category = CategorySerializer(many=True)
	class Meta:
		model = Article
		fields = [
			'title',
			'summary',
			'content',
			'authors',
			'category',
			'published_status',
			'published_date',
			'updated'
		]