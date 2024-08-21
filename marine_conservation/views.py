from django.shortcuts import render
from .models import MarineProtectedArea, EndangeredSpecies, ConservationInitiative


def home(request):
    return render(request, 'marine_conservation/home.html')


def protected_areas(request):
    protected_areas = MarineProtectedArea.objects.all()
    context = {'protected_areas': protected_areas}
    return render(request, 'marine_conservation/protected_areas.html', context)


def protected_area_detail(request, pk):
    protected_area = MarineProtectedArea.objects.get(pk=pk)
    context = {'protected_area': protected_area}
    return render(request, 'marine_conservation/protected_area_detail.html', context)


def endangered_species(request):
    endangered_species = EndangeredSpecies.objects.all()
    context = {'endangered_species': endangered_species}
    return render(request, 'marine_conservation/endangered_species.html', context)


def endangered_species_detail(request, pk):
    endangered_species = EndangeredSpecies.objects.get(pk=pk)
    context = {'endangered_species': endangered_species}
    return render(request, 'marine_conservation/endangered_species_detail.html', context)


def conservation_initiatives(request):
    conservation_initiatives = ConservationInitiative.objects.all()
    context = {'conservation_initiatives': conservation_initiatives}
    return render(request, 'marine_conservation/conservation_initiatives.html', context)


def conservation_initiative_detail(request, pk):
    conservation_initiative = ConservationInitiative.objects.get(pk=pk)
    context = {'conservation_initiative': conservation_initiative}
    return render(request, 'marine_conservation/conservation_initiative_detail.html', context)


def get_involved(request):
    # Add your logic to render the "Get Involved" page
    return render(request, 'marine_conservation/get_involved.html')


def team(request):
    return render(request, 'marine_conservation/team.html')
