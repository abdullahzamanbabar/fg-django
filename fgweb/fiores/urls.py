from django.urls import path
from . import views

app_name = 'fiores'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about', views.AboutView.as_view(), name="about"),
    path('team', views.TeamView.as_view(), name="team"),
    path('projects', views.ProjectsView.as_view(), name="projects"),
]
