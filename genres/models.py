from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)
    #description = models.TextField()

    def __str__(self) -> str:
        return self.name
