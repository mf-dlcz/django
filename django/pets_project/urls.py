from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("hello/", include("hello_app.urls"))
    path("", include("pets_app.urls"))
]