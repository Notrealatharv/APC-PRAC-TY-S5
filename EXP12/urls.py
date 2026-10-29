from django.urls import path
from . import views

urlpatterns = [
    path("password/", views.password, name="password"),
]
from django.urls import path, include

urlpatterns = [
    path("", include("yourapp.urls")),
]