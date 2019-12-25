import json
import logging

import datetime

import random
import string
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from brain import settings
from article.models import Article
from . import forms
from paypal.standard.forms import PayPalPaymentsForm


class Dashboard(
    LoginRequiredMixin,
    generic.DetailView
):
    model = User
    template_name = 'users/dashboard.html'

    def get_object(self, queryset=None):
        return self.request.user


class LogoutView(LoginRequiredMixin, generic.FormView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/logout.html', {})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            post_data.update({'user': request.user.pk})
            form = forms.LogoutForm(post_data)
            if form.is_valid():
                logout(self.request)
                return HttpResponseRedirect(reverse('home'))


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
    form_valid_message = 'User has been created successfully!'
    form_invalid_message = 'Something wrong'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                fd = form.cleaned_data
                username = fd['username']
                email = fd['email']
                password1 = fd['password1']
                password2 = fd['password2']
                if password1 == password2:
                    password = password1

                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    userObj = User.objects.create_user(username, email, password1)
                    userObj.first_name = fd['first_name']
                    userObj.last_name = fd['last_name']
                    userObj.save()
                    # user = authenticate(username=username, password=password)
                    # login(request, user)

                    return HttpResponseRedirect('/users/login')
                else:
                    return "This Email Already exists, Use another email address please!"

        else:
            form = forms.SignUpForm()

        return render(request, 'users/signup.html', {'form': form})


class Profile(generic.DetailView):
    form_class = forms.User
    template_name = 'users/profile.html'

    def get_object(self):
        return forms.User


class Tagging(LoginRequiredMixin, generic.DetailView):

    def get(self, request, *args, **kwargs):
        cat = self.kwargs.get('cat')
        queryset_list = Article.objects.filter(category=cat).exclude(articles__user=request.user).distinct()
        paginator = Paginator(queryset_list, 1)
        page_request_var = "article"
        page = request.GET.get(page_request_var)
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
        context = {
            'articles': queryset,
            'page_request_var': page_request_var,
        }

        return render(request, 'users/tagging.html', context)


class TagView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TagForm

    def post(self, request, *args, **kwargs):
        try:
            post_data = request.POST.copy()
            post_data.update({'user': request.user.pk})
            form = forms.TagForm(post_data)
            if form.is_valid():
                tag = form.save(commit=False)
                tag.user = request.user
                tag.email = request.user.email
                tag.save()
            else:
                return HttpResponse(form.errors, status=400)

            return HttpResponseRedirect(reverse_lazy('users:dashboard'))

        except Exception as exp:
            logging.error(exp)
            return HttpResponse(exp, status=400)


def generate_cid():
    chars = "".join([random.choice(string.ascii_lowercase) for i in range(5)])
    digits = "".join([random.choice(string.digits) for i in range(4)])
    cid = digits + chars
    return cid


def payment_process(request):
    minutes = int(request.user.tagging.count()) * 5
    testhours = minutes / 60
    hours = ''
    if request.user.tagging.count() > 11:
        hours = str(round(testhours, 3))
        if hours > str(5):
            hours = 5
    # invoice = generate_cid()
    user_info = {
        "name": str(request.user.first_name + ' ' + request.user.last_name),
        "hours": str(hours),
        "taggedArticles": str(request.user.tagging.count()),
        "email": str(request.user.email),
        "date": str(datetime.date.today()),
    }
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "item_name": "Certificate of Completion from Nami Montana",
        "custom": json.dumps(user_info),
        "invoice": str(generate_cid()),
        "amount": "95.00",
        "currency_code": "USD",
        "notify_url": settings.host + "/users/paypal/",
        "return_url": settings.host + "/users/done",
        "cancel_return": settings.host + "/users/cancel",
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "users/generateCert.html", context)


@csrf_exempt
def payment_done(request):
    user = request.user
    return render(request, 'users/payment_done.html', {'user': user})


@csrf_exempt
def payment_canceled(request):
    return render(request, 'users/payment_canceled.html')
