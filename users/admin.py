from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import TaggedArticle
from .models import TaggedArticle as Tagged

User = get_user_model()
admin.site.unregister(User)


class InlineTaggedArticle(admin.TabularInline):
    fields = ['category_fit', 'article', 'link', 'relevant_feedback', 'category', 'user', 'email']
    model = Tagged


class CustomAdmin(UserAdmin):
    # date_hierarchy = 'date_joined'
    inlines = [InlineTaggedArticle, ]
    list_display = list(UserAdmin.list_display) + ['totol_tagged_article']

    def totol_tagged_article(self, obj):
        return obj.tagging.all().count()


admin.site.register(User, CustomAdmin)


# Resource to export Tagged Articles
class TaggedArticleResource(resources.ModelResource):
    class Meta:
        model = TaggedArticle


class TaggedArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TaggedArticleResource
    date_hierarchy = 'created_at'
    fields = ['category_fit', 'article', 'link', 'relevant_feedback', 'category', 'user', 'email']
    list_display = ['article', 'link', 'user', 'email', 'relevant_feedback']
    list_filter = ['user', 'email']
    model = TaggedArticle


admin.site.register(Tagged, TaggedArticleAdmin)


