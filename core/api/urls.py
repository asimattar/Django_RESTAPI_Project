from django.urls import path
from . import views  # Absolute import for views

urlpatterns = [
    # Client Endpoints
    path('clients/', views.ClientView.as_view(), name='client-list-create'),  # For listing clients or creating a new one
    path('clients/<int:client_id>/', views.ClientView.as_view(), name='client-detail'),  # For getting, updating, or deleting a client

    # Project Endpoints
    path('clients/<int:client_id>/projects/', views.ProjectView.as_view(), name='project-list-create'),  # For creating a project for a client
    path('projects/', views.AssignedProjectsView.as_view(), name='project-list'),  # For listing all projects
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='project-detail'),  # For getting the details of a specific project
]
