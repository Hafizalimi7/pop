from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    age  = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE')
     )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    height = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


