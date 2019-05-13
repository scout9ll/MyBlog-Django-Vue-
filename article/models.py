from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Article_Type(models.Model):
    type_name = models.CharField(max_length=15)  # 用来显示，type_name=Article中的article_Type

    def __str__(self):
        return self.type_name


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)
    article_Type = models.ForeignKey(Article_Type, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
