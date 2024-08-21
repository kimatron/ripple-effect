from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('protected-areas/', views.protected_areas, name='protected_areas'),
    path('endangered-species/', views.endangered_species,
         name='endangered_species'),
    path('conservation-initiatives/', views.conservation_initiatives,
         name='conservation_initiatives'),
    path('get-involved/', views.get_involved, name='get_involved'),
]
