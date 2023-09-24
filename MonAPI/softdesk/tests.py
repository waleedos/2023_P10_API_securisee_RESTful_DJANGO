from django.test import TestCase
# Import de la classe TestCase du module django.test. Cette classe est la base pour tous les tests Django.

from .models import User, Project, Contributor
# Import des modèles User, Project, et Contributor depuis le fichier models.py dans le même répertoire.

from rest_framework.test import APITestCase
# Import de la classe APITestCase du module rest_framework.test. Cette classe est utilisée pour tester les API.

from rest_framework import status
# Importe du module status de rest_framework. Ce module contient des constantes HTTP pour les codes de statut.

import json


# -------------------------------------------------------------------------------------
# Test de création d'utilisateur
class UserTestCase(TestCase):
    # Définit une nouvelle classe de test UserTestCase qui hérite de TestCase.

    def setUp(self):
        User.objects.create_user(username="testuser", password="testpassword", age=20)
        # Définition de la méthode setUp qui est exécutée avant chaque test dans cette classe et Création d'un nouvel
        # utilisateur avec le nom d'utilisateur testuser, le mot de passe testpassword, et l'âge 20.

    def test_user_creation(self):
        #    Définition d'un test pour vérifier la création d'un utilisateur.

        user = User.objects.get(username="testuser")
        # Récupèration de l'utilisateur créé par son nom d'utilisateur.

        self.assertEqual(user.username, 'testuser')
        # Vérification que le nom d'utilisateur de l'objet récupéré est bien testuser.

# -------------------------------------------------------------------------------------


# Test d'authentification
class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', age=20)

    def test_authentication(self):
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/api/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# -------------------------------------------------------------------------------------

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

# -------------------------------------------------------------------------------------


# Test de validation de l'âge et du consentement
class UserValidationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        self.client.force_authenticate(user=self.user)  # Ajout de la simulation d'authentification

    def test_age_validation(self):
        data = {"username": "younguser", "password": "testpassword", "age": 14}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Vous devez avoir au moins 15 ans pour vous inscrire.', str(response.data))

    def test_consent_validation(self):
        data = {"username": "noconsentuser", "password": "testpassword", "age": 20, "consent": False}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data.get('consent'))

# -------------------------------------------------------------------------------------


class UserDataExportTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        self.client.force_authenticate(user=self.user)

    def test_user_data_export(self):
        response = self.client.get("/api/profile/export/")
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response_data)
        self.assertIn('email', response_data)
