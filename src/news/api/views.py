from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from news.models import *
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .pagination import CustomPageNumberPagination

class NewsArticleList(ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	pagination_class = CustomPageNumberPagination




class BookmarkArticle(APIView):
	permission_classes = [IsAuthenticated]
	def post(self,request):
		article_id = request.data.get("id")
		try:
			article_obj = Article.objects.get(id=article_id)
		except Article.DoesNotExist:
			return Response({"message":"Article not found.","success":False}, status=status.HTTP_404_NOT_FOUND)
		except ValueError:
			return Response({"message":"Invalid or empty article id.","success":False}, status=status.HTTP_400_BAD_REQUEST)

		bookmark_obj,created = UserBookmarks.objects.get_or_create(user=request.user)
	
		if article_obj in bookmark_obj.article.all():
			return Response({"message":"Article has already been bookmarked!","success":True}, status=status.HTTP_200_OK)
		else:
			bookmark_obj.article.add(article_obj)
			return Response({"message":"Article has been bookmarked successfully!","success":True}, status=status.HTTP_200_OK)


class RemoveBookmarkedArticle(APIView):
	permission_classes = [IsAuthenticated]
	def post(self,request):
		article_id = request.data.get("id")
		try:
			article_obj = Article.objects.get(id=article_id)
		except Article.DoesNotExist:
			return Response({"message":"Article not found.","success":False}, status=status.HTTP_404_NOT_FOUND)
		except ValueError:
			return Response({"message":"Invalid or empty article id.","success":False}, status=status.HTTP_400_BAD_REQUEST)

		bookmark_obj,created = UserBookmarks.objects.get_or_create(user=request.user)
		if article_obj in bookmark_obj.article.all():
			bookmark_obj.article.remove(article_obj)
			response_dict ={
				"message":"Article has been successfully removed from your bookmarks!",
				"success":True
			}
			return Response(response_dict, status=status.HTTP_200_OK)
		else:
			return Response({"success":False,"message":"Article not bookmarked yet."}, status=status.HTTP_400_BAD_REQUEST)










