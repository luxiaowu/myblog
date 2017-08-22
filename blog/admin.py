from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'createtime')
    list_filter = ('createtime',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)