from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, editable=False)
    published_date = models.DateField()

    def __str__(self):
        return self.title
