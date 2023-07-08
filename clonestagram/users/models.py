from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    display_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.email
