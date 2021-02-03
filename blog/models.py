from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

