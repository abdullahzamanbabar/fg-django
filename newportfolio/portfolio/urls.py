from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('projects', views.ProjectsView.as_view(), name="projects"),
    # path('projects', views.ProjectsView.as_view(), name="projects"),
]
