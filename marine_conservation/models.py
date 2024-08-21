from django.db import models

# Create your models here.


class MarineProtectedArea(models.Model):
    name = models.CharField(max_length=100)  # Name of the protected area
    # Location (e.g., coordinates or region)
    location = models.CharField(max_length=200)
    # Type of ecosystem (e.g., Coral Reef, Mangrove)
    ecosystem_type = models.CharField(max_length=100)
    # Status (e.g., Protected, Endangered)
    conservation_status = models.CharField(max_length=50)
    description = models.TextField()  # Detailed information about the area
    # Image for visual representation
    image = models.ImageField(
        upload_to='protected_areas', null=True, blank=True)

    def __str__(self):
        return self.name  # This returns the name of the protected area when the object is printed


class EndangeredSpecies(models.Model):
    name = models.CharField(max_length=100)  # Name of the species
    species_type = models.CharField(max_length=50)  # Type (e.g., Fish, Mammal)
    # Status (e.g., Endangered, Critically Endangered)
    conservation_status = models.CharField(max_length=50)
    # Typical habitat of the species
    habitat = models.CharField(max_length=200)
    description = models.TextField()  # Detailed information about the species
    image = models.ImageField(
        upload_to='endangered_species', null=True, blank=True)  # Image of the species

    def __str__(self):
        return self.name  # Returns the name of the species when the object is printed


class ConservationInitiative(models.Model):
    name = models.CharField(max_length=100)  # Name of the initiative
    # Organization leading the initiative
    organization = models.CharField(max_length=100)
    description = models.TextField()  # Detailed description of the initiative
    website = models.URLField()  # Link to the official website or additional resources
    # Image representing the initiative
    image = models.ImageField(
        upload_to='conservation_initiatives', null=True, blank=True)

    def __str__(self):
        return self.name  # Returns the name of the initiative when the object is printed
