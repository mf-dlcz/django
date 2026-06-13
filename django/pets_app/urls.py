from django.urls import path
from pets_app import views

urlpatterns = [
    path('pets/', views.listPets, name='petsList'),
]