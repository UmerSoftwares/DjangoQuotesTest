from django.db import models
from django.core.validators import MaxLengthValidator


class Quote(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)])
