from django.db import models
from authentication.models import User


class Groups(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_user')


class ToDos(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    is_active = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    due_date = models.DateField()
    groups = models.OneToOneField(Groups, on_delete=models.CASCADE, related_name='todos')







