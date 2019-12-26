from django import template

from blog.models import PostModel

register = template.Library()


@register.inclusion_tag('blog/recent_blog_posts.html')
def recent_posts():
    recent_blogs = PostModel.objects.all().order_by('-created_at')[:5]
    return {'recent_posts': recent_blogs}
