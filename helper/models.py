from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Helper(models.Model):
    helper = models.CharField(max_length=100, default="")
    helper_rank = models.CharField(max_length=100, default="")
    helper_point = models.CharField(max_length=100, default="")
    date_posted = models.DateTimeField(default=timezone.now)   

    def __str__(self):
        return self.helper

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
