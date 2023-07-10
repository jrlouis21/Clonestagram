from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    display_name = models.CharField(max_length=30, null=False)
    profile_picture = models.ImageField(null=True, upload_to="static/photos")
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    bio = models.TextField(max_length=150, blank=True, default="Bio")
    website = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.email
