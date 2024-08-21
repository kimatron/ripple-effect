from django.db import models

# Create your models here.


class MarineProtectedArea(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    ecosystem_type = models.CharField(max_length=100)
    conservation_status = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(
        upload_to='protected_areas', null=True, blank=True)

    def __str__(self):
        return self.name


class EndangeredSpecies(models.Model):
    name = models.CharField(max_length=100)
    species_type = models.CharField(max_length=50)
    conservation_status = models.CharField(max_length=50)
    habitat = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='endangered_species', null=True, blank=True)

    def __str__(self):
        return self.name


class ConservationInitiative(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    image = models.ImageField(
        upload_to='conservation_initiatives', null=True, blank=True)

    def __str__(self):
        return self.name
