from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('protected-areas/', views.protected_areas_list, name='protected_areas'),
    path('protected-areas/<int:pk>/', views.protected_area_detail,
         name='protected_area_detail'),
    path('endangered-species/', views.endangered_species_list,
         name='endangered_species'),
    path('endangered-species/<int:pk>/', views.endangered_species_detail,
         name='endangered_species_detail'),
    path('conservation-initiatives/', views.conservation_initiatives_list,
         name='conservation_initiatives'),
    path('conservation-initiatives/<int:pk>/',
         views.conservation_initiative_detail, name='conservation_initiative_detail'),
]
