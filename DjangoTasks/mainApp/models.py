from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Ownable(models.Model):
    user = models.ForeignKey('auth.User', verbose_name="Author",
                             related_name="%(class)ss", on_delete=CASCADE)

    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    post_authors = models.ForeignKey('auth.User', on_delete=CASCADE,
                                     related_name='post_authors')
    user = models.OneToOneField(User, on_delete=CASCADE)

class FeedItem(Ownable):
    content = models.CharField("Content", max_length=1000,
                               blank=True, null=True)
