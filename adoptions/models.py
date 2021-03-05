from django.db import models


class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)  # null setting to True means that age is unknown
    vaccinations = models.ManyToManyField('Vaccine',
                                          blank=True)  # Since each pet can have many vaccines and one vaccine can be
    # given to many pets
    # So vaccination field is given manytomany relationship from Pet model to Vaccine model


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
