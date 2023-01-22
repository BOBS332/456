from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг пользователя',
        default=0,
    )

    @property
    def full_name(self):
        return ' '.join((self.last_name, self.first_name))
