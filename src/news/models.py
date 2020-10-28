from django.db import models
from django.conf import settings
# Create your models here.

class Article(models.Model):
	ARTICLE_PUBLISHING_STATUSES = (
		("PENDING", "PENDING"),
		("DRAFT", "DRAFT"),
		("PUBLISHED", "PUBLISHED"),
		("UNPUBLISHED", "UNPUBLISHED"),
	)
	title = models.CharField(max_length=100)
	summary =  models.CharField(max_length=250)
	content = models.TextField()
	authors = models.ManyToManyField('Author')
	category = models.ManyToManyField('Category')
	published_status = models.CharField(choices=ARTICLE_PUBLISHING_STATUSES,max_length=30,default="PUBLISHED")
	published_date = models.DateTimeField()
	updated =  models.DateTimeField(auto_now=True, auto_now_add=False)


	def __str__(self):
		return self.title



class Author(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class UserBookmarks(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	article = models.ManyToManyField(Article)

	def __str__(self):
		return self.user.username