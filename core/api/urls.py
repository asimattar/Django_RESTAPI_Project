from django.urls import path
from . import views  

urlpatterns = [
    # Client Endpoints
    path('clients/', views.ClientView.as_view(), name='client-list-create'),  
    path('clients/<int:client_id>/', views.ClientView.as_view(), name='client-detail'),  

    # Project Endpoints
    path('clients/<int:client_id>/projects/', views.ProjectView.as_view(), name='project-list-create'),  
    path('projects/', views.AssignedProjectsView.as_view(), name='project-list'),  
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='project-detail'),  
]
