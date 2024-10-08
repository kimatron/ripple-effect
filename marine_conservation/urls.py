from django.conf import settings
from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('protected-areas/', views.protected_areas, name='protected_areas'),
    path('protected-areas/<int:pk>/', views.protected_area_detail,
         name='protected_area_detail'),
    path('endangered-species/', views.endangered_species,
         name='endangered_species'),
    path('endangered-species/<int:pk>/', views.endangered_species_detail,
         name='endangered_species_detail'),
    path('conservation-initiatives/', views.conservation_initiatives,
         name='conservation_initiatives'),
    path('conservation-initiatives/<int:pk>/',
         views.conservation_initiative_detail, name='conservation_initiative_detail'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('team/', views.team, name='team'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
