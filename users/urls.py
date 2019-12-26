from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views
# from article import urls as article_detail

app_name = 'users'

urlpatterns = [
   path('paypal/', include('paypal.standard.ipn.urls')),
   path('cancel/', views.PaymentCanceled.as_view(), name='cancel'),
   path('process/', views.payment_process, name='payment'),
   path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   path('signup/', views.SignUpView.as_view(), name='signup'),
   path('login/', auth_views.LoginView.as_view(), name='login'),
   path('profile/', views.Profile.as_view(), name='profile'),
   # url(r'^profile/cert$', views.CertReturn.as_view(), name='cert'),
   # re_path(r'^tagging/(?P<cat>(?=.*\S).+)/', views.Tagging.as_view(), name='tagging'),
   # path(r'article/tag/', views.TagView.as_view(), name='tagged'),
   # path(r'article/', include(article_detail)),
   path('', include('django.contrib.auth.urls')),
]

