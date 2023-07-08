from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone

User = get_user_model()


class Post(models.Model):
    timestamp = models.DateTimeField(editable=False)
    edited = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    caption = models.TextField()
    likes = GenericRelation("Like")

    def save(self, *args, **kwargs):
        """
        Custom save function to add timestamp when a Post is saved to the database.
        """
        if not self.id:
            self.timestamp = timezone.now()

        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.display_name} - {self.caption}"


class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="photos")


class Comment(models.Model):
    timestamp = models.DateTimeField(editable=False)
    edited = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    likes = GenericRelation("Like")

    def save(self, *args, **kwargs):
        """
        Custom save function to add timestamp when a comment is saved to the database.
        """
        if not self.id:
            self.timestamp = timezone.now()

        return super(Comment, self).save(*args, **kwargs)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    like = models.BooleanField(default=True)
