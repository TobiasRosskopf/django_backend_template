from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# from django.db import models


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = "Nutzer"
        verbose_name_plural = "Nutzer"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"


class CustomGroup(Group):

    class Meta:
        verbose_name = "Gruppe"
        verbose_name_plural = "Gruppen"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
