# Importation des modules nécessaires de Django REST Framework et de Django
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

# Importation des modèles de l'application
from .models import Project, Contributor, Issue, Comment


# Définition du serializer pour la création d'un nouvel utilisateur (Signup)
class SignupSerializer(ModelSerializer):

    # Le champ date_joined est en lecture seule
    date_joined = serializers.ReadOnlyField()

    # Métadonnées du serializer
    class Meta:
        # Modèle associé
        model = User
        # Champs à sérialiser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'date_joined')
        # Le mot de passe sera en écriture seule (pas renvoyé par l'API)
        extra_kwargs = {'password': {'write_only': True}}

    # Méthode pour créer un nouvel utilisateur
    def create(self, data):
        return User.objects.create_user(**data)


# Serializer pour le modèle Project
class ProjectSerializer(serializers.ModelSerializer):
    # Champ author avec une clé primaire, mais non requis
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Project  # Modèle associé
        fields = '__all__'  # Sérialisation de tous les champs


# Serializer pour le modèle Contributor
class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor  # Modèle associé
        fields = '__all__'  # Sérialisation de tous les champs


# Serializer pour le modèle Issue
class IssueSerializer(ModelSerializer):
    # Champ project et assignee non requis
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), required=False)
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Issue  # Modèle associé
        fields = '__all__'  # Sérialisation de tous les champs


# Serializer pour le modèle Comment
class CommentSerializer(ModelSerializer):
    # Champ issue non requis
    issue = serializers.PrimaryKeyRelatedField(queryset=Issue.objects.all(), required=False)

    class Meta:
        model = Comment  # Modèle associé
        fields = '__all__'  # Sérialisation de tous les champs
