from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from slugify import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()  # Using TinyMCE's HTMLField instead of RichTextUploadingField
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image', default="image/default.jpg")

    def save(self, *args, **kwargs):
        
        if self.image:
            filename = self.image.name
            ext = filename.split('.')[-1]  # Extracts extension from filename
            filename = '{}.{}'.format(slugify(filename.replace('.' + ext, '')), ext)  # Replaces filename with slugified version
            self.image.name = filename
            print("hello")
            if self.pk:
                old_img = Post.objects.get(pk=self.pk).image
                if old_img.name != filename:
                    old_img.delete(save=False)  # Deletes the old image file from storage if it has changed
                    print("hello2")
                print("hello3")
        super(Post, self).save(*args, **kwargs)
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
