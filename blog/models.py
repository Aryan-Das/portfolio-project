from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

