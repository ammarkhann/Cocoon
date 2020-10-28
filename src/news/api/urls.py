from django.conf.urls import url
from django.contrib import admin

from news.api.views import *

from django.urls import path,include

urlpatterns = [
	
	path('',NewsArticleList.as_view(),name="news_article_list"),
	path('article/bookmark/add/',BookmarkArticle.as_view(),name="bookmark_article"),
	path('article/bookmark/remove/',RemoveBookmarkedArticle.as_view(),name="remove_bookmarked_article"),

]
