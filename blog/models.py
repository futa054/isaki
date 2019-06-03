from django.db import models

class Blog(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(upload_to = 'images')
    posted_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)