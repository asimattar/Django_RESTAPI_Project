from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class ClientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, client_id=None):
        if client_id:
            client = Client.objects.get(id=client_id)
            serializer = ClientSerializer(client)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, client_id):
        client = Client.objects.get(id=client_id)
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id):
        client = Client.objects.get(id=client_id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        data['client'] = client.id  

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save(created_by=request.user)
            response_data = ProjectSerializer(project).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignedProjectsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = request.user.assigned_projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
