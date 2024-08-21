from django.shortcuts import render


def home(request):
    return render(request, 'marine_conservation/base.html')


def protected_areas(request):
    # Add your logic to render the protected areas page
    return render(request, 'marine_conservation/protected_areas.html')


def endangered_species(request):
    # Add your logic to render the endangered species page
    return render(request, 'marine_conservation/endangered_species.html')


def conservation_initiatives(request):
    # Add your logic to render the conservation initiatives page
    return render(request, 'marine_conservation/conservation_initiatives.html')


def get_involved(request):
    # Add your logic to render the "Get Involved" page
    return render(request, 'marine_conservation/get_involved.html')
