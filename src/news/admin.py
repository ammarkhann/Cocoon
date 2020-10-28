from django.contrib import admin
from .models import (

	Article,
	Author,
	Category,
	UserBookmarks,


)
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(UserBookmarks)
