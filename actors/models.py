from django.db import models


NATIONALITY_CHOICES = (
    ('BRAZIL', 'Brasil'),
    ('USA', 'Estados Unidos'),
    ('CHILE', 'Chile'),
)

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100,
                                   choices=NATIONALITY_CHOICES,
                                   blank=True,
                                   null=True)
    
    def __str__(self) -> str:
        return self.name
    

