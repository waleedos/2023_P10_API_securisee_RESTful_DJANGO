from django.test import TestCase
from .models import User, Project, Contributor  # Importez les modèles nécessaires
from rest_framework.test import APITestCase
from rest_framework import status


# Test de création d'utilisateur
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testuser", password="testpassword", age=20)

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.username, 'testuser')


# Test d'authentification
class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', age=20)

    def test_authentication(self):
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/api/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Test de création de projet
class ProjectTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        self.client.force_authenticate(user=self.user)
        self.project = Project.objects.create(
            name="Test Project",
            description="Test Description",
            type="back-end",
            author=self.user
        )
        # Ajout du contributeur
        Contributor.objects.create(user=self.user, project=self.project)

    def test_create_project(self):
        data = {
            "name": "Test Project",
            "description": "Test Description",
            "type": "back-end",
            "author": self.user.id
        }
        response = self.client.post("/api/projects/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_contributor(self):
        data = {"username": self.user.username}
        response = self.client.post(f"/api/projects/{self.project.id}/add_contributor/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_contributor(self):
        data = {"username": self.user.username}
        response = self.client.post(f"/api/projects/{self.project.id}/remove_contributor/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_access_project(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(f'/api/projects/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_project_data(self):
        data = {
            "name": "",
            "description": "Test Description",
            "type": "back-end",
            "author": self.user.id
        }
        response = self.client.post("/api/projects/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
