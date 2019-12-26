from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .forms import PostForm, CommentForm
from .models import PostModel, CommentModel


def home(request):
    """
    The home function loads the main page for Blog to see blog posts..
    This will load the page with all main features of the Blog as:
    Search - to search the blog posts by using keywords
    filtering - To filter the blog posts by categories.
    """

    posts = PostModel.objects.all().order_by('-created_at')
    try:
        recent_posts = PostModel.objects.all().order_by('-created_at')[:5]
    except:
        recent_posts = None
    return render(request, 'blog/blog_home.html', {'posts': posts, 'recent': recent_posts})


def search(request):
    posts = PostModel.objects.filter(title__contains=request.GET['title'])
    return render(request, 'blog/blog_home.html', {'posts': posts})


def category(request, link):
    categories = {
        'brain-research-tagging-news': 'BRTN',
        'brain-health-news': 'BHN',
        'research-domain-criteria-news': 'RDCN',
    }
    try:
        posts = PostModel.objects.filter(category=categories[link])
        cat = categories[link]
        return render(request, 'blog/blog_home.html', {'posts': posts, 'cat': cat})
    except KeyError:
        return redirect('blog-home')


def post_detail(request, pk):
    try:
        post = PostModel.objects.get(id=pk)
        comments = CommentModel.objects.filter(post_id=pk, reply=None).order_by('-id')
        return render(request, 'blog/post.html', {'object': post, 'comments': comments})
    except PostModel.DoesNotExist:
        return redirect(reverse('blog-home'))


class PostCreate(generic.CreateView):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'blog/postmodel_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            post_data = request.POST.copy()
            post_data.update({'author': request.user.pk})
            form = PostForm(post_data, request.FILES)
            print(post_data)
            try:
                if form.is_valid():
                    blog_post = form.save(commit=False)
                    blog_post.author = request.user
                    blog_post.save()
                    return HttpResponseRedirect(reverse('blog-home'))
                else:
                    print(form.errors)
                    return HttpResponse('something bas in invalid')
            except Exception as e:
                print(e)
        return HttpResponseRedirect(reverse('blog-home'))


def delete_post(request, pk):
    if request.method == 'GET':
        try:
            blog_post = PostModel.objects.get(id=pk)
            blog_post.delete()
            return HttpResponseRedirect(reverse('blog-home'))
        except PostModel.DoesNotExist:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect(reverse('blog-home'))


def comment(request):
    if request.method == 'POST':
        cmt_form = CommentForm(request.POST or None)
        if cmt_form.is_valid():
            post_id = request.POST.get('post')
            post = PostModel.objects.get(id=post_id)
            content = request.POST.get('content')
            print(post_id)
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = CommentModel.objects.get(id=reply_id)
            comment_obj = CommentModel.objects.create(content=content, author=request.user,
                                                      post=post, reply=comment_qs)
            comment_obj.save()
            return redirect('blog-post', pk=post_id)
