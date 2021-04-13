from django.db import models
from django.utils import timezone


class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    video_file = models.FileField(upload_to='films/%Y/%m/%d/')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
