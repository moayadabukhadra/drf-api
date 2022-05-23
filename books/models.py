from django.db import models
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=64)
    publish_Date = models.DateField(null=True)
    reviewer = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)


    def __str__(self):
        return self.title