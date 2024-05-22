from django import forms
from .models import Comment, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from tinymce.widgets import TinyMCE
from django.core.exceptions import ValidationError
import re
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('title', css_class='my-title-class'),
            Field('content', css_class='my-content-class'),
            Field('image', css_class='my-image-class'),
            Submit('submit', 'Submit', css_class='btn-success')
        )
    