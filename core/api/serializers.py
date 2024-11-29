from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    created_by = serializers.SerializerMethodField()  

    class Meta:
            model = Project
            fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def get_created_by(self, obj):
        
        return obj.created_by.username

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.SerializerMethodField()  

    class Meta:
        model = Client
        fields = ['id', 'projects', 'client_name', 'created_at', 'updated_at', 'created_by']

    def get_created_by(self, obj):
        
        return obj.created_by.username  
