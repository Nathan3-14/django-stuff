import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_body = models.CharField(max_length=300)
    post_pub_date = models.DateTimeField("Date Published")

    def __str__(self):
        return self.post_title

    def was_recent(self):
        return self.post_pub_date >= timezone.now() - datetime.timedelta(days=1)
