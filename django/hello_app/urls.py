from django.urls import path, include
from hello_app import views

urlpatterns = [
    path("", views.sayHello)
]