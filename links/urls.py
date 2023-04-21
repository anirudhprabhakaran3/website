from django.urls import path
from links import views

urlpatterns = [
    path('<str:slug>', views.pattern_matcher, name="pattern_matcher"),
    path('', views.index, name="short_links_home"),
]
