from django.conf import settings
from django.db import models
from django.utils import timezone


class Hashtag(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text