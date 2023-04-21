from django.urls import path
from links import views

urlpatterns = [
    path("<str:slug>", views.unshorten, name="unshorten")
]
