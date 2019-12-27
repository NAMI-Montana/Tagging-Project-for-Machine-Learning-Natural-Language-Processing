from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from paypal.standard.models import ST_PP_COMPLETED

from article.models import Article
from django.utils import timezone

choices = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('not sure', 'Not Sure'),
)


class TaggedArticle(models.Model):
    user = models.ForeignKey(User, related_name='tagging', on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    category_fit = models.CharField(choices=choices, max_length=255)
    article = models.ForeignKey(Article, related_name='articles', on_delete=models.CASCADE)
    link = models.URLField(max_length=255, )
    relevant_feedback = models.TextField(blank=True)
    category = models.CharField(max_length=255, )
    created_at = models.DateTimeField(default=timezone.now, editable=False)
