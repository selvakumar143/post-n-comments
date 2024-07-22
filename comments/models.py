from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from blog.models import BlogPost

class Comment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'P', _('Pending')
        APPROVED = 'A', _('Approved')
        REJECTED = 'R', _('Rejected')

    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    comments = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.title
