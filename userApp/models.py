from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
#from trainingApp.models import Group  # Importa Group desde trainingApp

class Trainee(models.Model):
    #Enumeracion para el nivel educativo del user
    class EducationalLevel(models.TextChoices):
        Primary_School = 'Primary School', _('Primary School')
        High_School = 'High School', _('High School')
        Associate  = 'Associate', _('Associate')
        University  = 'University', _('University')
        Doctoral_Student  = 'Doctoral Student', _('Doctoral Student')
        Magister  = 'Magister', _('Magister')
        Doctor  = 'Doctor', _('Doctor')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age =  models.IntegerField(default=18)
    educationalLevel = models.CharField(
        max_length=50,
        choices=EducationalLevel.choices,
        default=EducationalLevel.High_School
    )
    occupation = models.CharField(max_length=50)
    group =  models.ForeignKey('trainingApp.Group', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Trainee_Id: {self.id}, Name Trainee: {self.user.first_name} {self.user.last_name}"
