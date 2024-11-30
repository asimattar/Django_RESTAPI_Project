from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class UserWithNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.SerializerMethodField()  

    class Meta:
        model = User
        fields = ['id', 'name']
    
    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() if obj else ""

    def create(self, validated_data):

        user, created = User.objects.get_or_create(id=validated_data['id'])
        user.first_name = validated_data.get('name', '')  
        user.save()
        return user
    

class ProjectSerializer(serializers.ModelSerializer):
    users = UserWithNameSerializer(many=True)  
    created_by = serializers.SerializerMethodField()  

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def get_created_by(self, obj):
     
        return obj.created_by.get_full_name()  

    def create(self, validated_data):

        users_data = validated_data.pop('users', [])
        project = Project.objects.create(**validated_data)

        for user_data in users_data:
            user = User.objects.get(id=user_data['id'])  
            user.first_name = user_data.get('name', '') 
            user.save()

            project.users.add(user) 

        project.save()
        return project
        

class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    created_by = serializers.SerializerMethodField()  

    class Meta:
        model = Client
        fields = ['id', 'projects', 'client_name', 'created_at', 'updated_at', 'created_by']

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.get_full_name()
        return None  

    def create(self, validated_data):
        request = self.context.get('request')  
        if request and request.user.is_authenticated:  
            validated_data['created_by'] = request.user  
        return super().create(validated_data)  
