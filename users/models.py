from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
    

# class UserLog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
#     action_time = models.DateField(auto_now_add=True)
#     action = models.CharField(max_length=20, verbose_name='action_name')
#     meta = models.CharField(max_length=150)

#     def __str__(self):
#         return self.action