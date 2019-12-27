from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    CAT_CHOICES = (
        ('BRTN', 'Brain Research Tagging News'),
        ('BHN', 'Brain Health News'),
        ('RDCN', 'Research Domain Criteria News'),
    )

    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField(config_name='default')
    photo = models.FileField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now=timezone.now())
    category = models.CharField(choices=CAT_CHOICES, max_length=100, blank=False, default='Default')

    def __str__(self):
        return self.title

    @property
    def get_last_5(self):
        return self.objects.all().order_by('-created_at')[:5]


class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1500, blank=
    False)
    reply = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment on {self.post.title} by {self.author.username}'
