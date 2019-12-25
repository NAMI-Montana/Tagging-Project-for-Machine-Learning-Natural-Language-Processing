from import_export import resources
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from users.models import TaggedArticle

# Create your views here.


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article
        # import_id_fields = ('id',)


class ArticleDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'article/articles.html'

    def get(self, request, *args, **kwargs):
        article_id = self.kwargs.get('id')
        article = TaggedArticle.objects.all().filter(id=article_id)
        # print(article)

        return render(request, 'article/articles.html', {'articles': article})



