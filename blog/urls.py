from django.urls import path, re_path

from .views import home, search, post_detail, \
    PostCreate, delete_post, category, comment

urlpatterns = [
    path('', home, name='blog-home'),
    path('search/', search, name='search'),
    path('post/<int:pk>', post_detail, name='blog-post'),
    re_path('category/(?P<link>[\w|-]+)/$', category, name='category'),
    path('post/new', PostCreate.as_view(), name='new-post'),
    path('post/delete/<int:pk>', delete_post, name='delete-post'),
    path('comment/new', comment, name='new-comment'),
]

# if settings.DEBUG:
#     urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
