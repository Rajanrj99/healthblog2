from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()  # Using TinyMCE's HTMLField instead of RichTextUploadingField
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image', default="image/default.jpg")

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()
