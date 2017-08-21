from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
	articles = models.Article.objects.all()
	return render(request, 'index.html', {'articles': articles})

def article(request, id):
	article = models.Article.objects.get(pk=id)
	return render(request, 'article.html', {'article': article})