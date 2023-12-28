from django.db import models
from django.contrib.auth.models import User


class Trainee(models.Model):
    #Nivel educativo del usuario
    class EducationalLevel(models.TextChoices):
        Primary_School = 'Primary'
        High_School = 'High School'
        Collage = 'Collage'
        Doctoral = 'Doctoral Student'
        Graduate = 'Ph.D'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    educationalLevel = models.CharField(
        max_length=20,
        choices=EducationalLevel.choices,
        default=EducationalLevel.High_School
    )
    occupation = models.CharField(max_length=50)