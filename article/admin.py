from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Article
from . import views
# Register your models here.


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    resource_class = views.ArticleResource
#    readonly_fields = ('id',)
