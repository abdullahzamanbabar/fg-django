from django.urls import path
from . import views

app_name = 'CompanyApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about', views.AboutView.as_view(), name="about"),
    path('projects', views.ProjectsView.as_view(), name="projects"),
    path('team', views.TeamView.as_view(), name="team"),
    path('story', views.StoryView.as_view(), name="story"),
]
