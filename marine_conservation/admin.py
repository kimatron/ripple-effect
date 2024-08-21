from django.contrib import admin
from .models import MarineProtectedArea, EndangeredSpecies, ConservationInitiative

admin.site.register(MarineProtectedArea)
admin.site.register(EndangeredSpecies)
admin.site.register(ConservationInitiative)
