from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models


# Create your views here.
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article(request, id):
    article = models.Article.objects.get(pk=id)
    return render(request, 'article.html', {'article': article})


def edit(request, id):
    if id:
        article = models.Article.objects.get(pk=id)
        return render(request, 'edit.html', {'article': article})
    return render(request, 'edit.html')


def edit_action(request, id):
    title = request.POST['title']
    content = request.POST.get('content', 'content')
    if id:
        article = models.Article.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()
        return HttpResponseRedirect('/blog/%s'%id)
    models.Article.objects.create(title=title, content=content)
    return HttpResponseRedirect('/blog')
