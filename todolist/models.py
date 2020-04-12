from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    