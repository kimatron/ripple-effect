from django.shortcuts import render


def home(request):
    return render(request, 'marine_conservation/base.html')
