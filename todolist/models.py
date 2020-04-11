from django.db import models


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
