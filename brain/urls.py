import django
from django.conf.urls import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, re_path, include
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^paypal/', include('paypal.standard.ipn.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('', lambda request: redirect('about/'), name='home'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static.static(django.conf.settings.MEDIA_URL, document_root=django.conf.settings.MEDIA_ROOT)


