from django.contrib.auth.models import AbstractUser
from django.db import models

BOARD_STATUS = [
    ('OPEN', 'OPEN'),
    ('COMPLETE', 'COMPLETE')
]

TASK_STATUS = [
    ('OPEN', 'OPEN'),
    ('INPROGRESS', 'INPROGRESS'),
    ('COMPLETE', 'COMPLETE')
]


# Create your models here.
class User(AbstractUser):
    display_name = models.CharField(max_length=64, null=True)
    description = models.CharField(max_length=128, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_user')
    users = models.ManyToManyField(User, related_name='users')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')
    status = models.CharField(choices=TASK_STATUS, default='OPEN', max_length=15)
    board = models.ForeignKey("Boards", on_delete=models.CASCADE, related_name="board")
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Boards(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(choices=BOARD_STATUS, default='OPEN', max_length=15)
    task = models.ManyToManyField(Tasks, related_name='tasks')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name