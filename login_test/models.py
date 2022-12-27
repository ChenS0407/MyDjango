from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    User = models.OneToOneField(User, models.CASCADE)  # CASCADE 级联删除
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.User.username