from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 

from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment

class SignupSerializer(ModelSerializer):

    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'username','email', 'password','date_joined')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        return User.objects.create_user(**data)


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Project
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'


class IssueSerializer(ModelSerializer):

    # project and assignee are not required - if yes, we cannot create new issue
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Issue
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = '__all__'



