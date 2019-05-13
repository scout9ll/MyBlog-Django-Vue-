from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Article, Article_Type   #.model 意为在此目录下找models 、..是上级目录
# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    Article_Types = Article_Type.objects.all()

    context = {"articles": articles,"Article_Types": Article_Types}
    return render(request, "article_list.html", context)
def article_detail(request,article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {"article_obj": article}
    return render(request, "article_detail.html", context)


def article_types(request):
    Article_Types = Article_Type.objects.all()
    context = {"Article_Types": Article_Types}
    return render(request, "article_types.html", context)


def article_type(request, type_id):
    article_type= get_object_or_404(Article_Type, pk=type_id)
    article = Article.objects.filter(article_Type=article_type)
    context = {"article_types":article}
    return render(request, "article_type.html",context)

