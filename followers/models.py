from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
    )

    followed_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers",
    )

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"
