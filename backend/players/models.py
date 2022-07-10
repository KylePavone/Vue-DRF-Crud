from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=120)
    game = models.CharField(max_length=120)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
