from django.contrib import admin
from .models import Article, Article_Type


# Register your models here.告诉对象需要被管理
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "article_Type", "is_deleted", "created_time", "last_updated_time")
    ordering = ("-id",)


class Article_TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Article_Type)
