from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
