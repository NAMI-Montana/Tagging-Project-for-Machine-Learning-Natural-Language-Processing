from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms.models import ModelForm

from .models import PostModel, CommentModel


class PostForm(ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = PostModel
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content', ]
