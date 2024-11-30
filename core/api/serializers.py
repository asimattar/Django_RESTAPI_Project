from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserWithNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.SerializerMethodField()  # Use get_full_name method

    class Meta:
        model = User
        fields = ['id', 'name']
    
    def get_name(self, obj):
        # Safely construct full name
        return f"{obj.first_name} {obj.last_name}".strip() if obj else ""

    def create(self, validated_data):
        # Custom logic to create or update user if needed
        user, created = User.objects.get_or_create(id=validated_data['id'])
        user.first_name = validated_data.get('name', '')  # Assign 'name' to 'first_name'
        user.save()
        return user

class ProjectSerializer(serializers.ModelSerializer):
    users = UserWithNameSerializer(many=True)  # Users are handled manually
    created_by = serializers.SerializerMethodField()  # To get the user's name who created the project

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def get_created_by(self, obj):
        # Return the full name of the user who created the project
        return obj.created_by.get_full_name()  # Adjusted to get full name

    def create(self, validated_data):
        # Custom logic to create a project and handle users
        users_data = validated_data.pop('users', [])
        project = Project.objects.create(**validated_data)

        for user_data in users_data:
            user = User.objects.get(id=user_data['id'])  # Find the user by ID
            user.first_name = user_data.get('name', '')  # Assign 'name' to 'first_name'
            user.save()

            project.users.add(user)  # Add user to the project

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
        return None  # Return None or a default value if created_by is not set

    def create(self, validated_data):
        request = self.context.get('request')  # Access the request object from context
        if request and request.user.is_authenticated:  # Ensure the user is authenticated
            validated_data['created_by'] = request.user  # Assign the logged-in user as created_by
        return super().create(validated_data)  # Adjusted to get full name (first_name + last_name)
