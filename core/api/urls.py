from django.urls import path
from .views import ClientView, AssignedProjectsView, ProjectView

urlpatterns = [
    path('clients/', ClientView.as_view()),
    path('clients/<int:client_id>/', ClientView.as_view()),
    path('clients/<int:client_id>/projects/', ProjectView.as_view()),
    path('projects/', AssignedProjectsView.as_view()),
]
