from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    banner_image = models.ImageField(upload_to='https://avatars.mds.yandex.net/i?id=e08f6247e771d383900ab3042ef84f87acea2940-12423213-images-thumbs&n=13', null=True, blank=True)

    def __str__(self):
        return self.title

