from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view/(?P<id>[-\w]+)/$', views.ArticleDetail.as_view(), name='article-detail'),
]