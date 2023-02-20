from django.db import models
class Author(models.Model):
    name = models.CharField(
        default='NoName',
        max_length=64,
        verbose_name='name of author'
    )