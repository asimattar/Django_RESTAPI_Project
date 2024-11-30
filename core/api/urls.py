from django.urls import path
from .views import ClientView, AssignedProjectsView, ProjectView

urlpatterns = [
    path('clients/', ClientView.as_view(), name='client-list-create'),
    path('clients/<int:client_id>/', ClientView.as_view(),name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectView.as_view()),
    path('projects/', AssignedProjectsView.as_view()),
]
