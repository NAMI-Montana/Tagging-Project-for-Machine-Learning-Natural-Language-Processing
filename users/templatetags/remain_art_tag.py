from django import template
# from article.models import Article
register = template.Library()


@register.inclusion_tag('users/profile.html')
def rem_tags(val):
    return 12 - val
