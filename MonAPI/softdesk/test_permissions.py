from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Project, Issue, Comment


class PermissionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = get_user_model().objects.create_user(username='user1', password='testpass123', age=30)
        self.user2 = get_user_model().objects.create_user(username='user2', password='testpass123', age=30)

        # Ajout de JWT pour l'authentification
        token = RefreshToken.for_user(self.user1)
        str_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str_token}')

        self.project = Project.objects.create(name='Project 1', author=self.user1)
        self.issue = Issue.objects.create(name='Issue 1', author=self.user1, project=self.project)
        self.comment = Comment.objects.create(description='Comment 1', author=self.user1, issue=self.issue)

    def test_non_contributor_cannot_edit_project(self):
        token = RefreshToken.for_user(self.user2)
        str_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str_token}')
        response = self.client.put(f'/api/projects/{self.project.id}/', {'name': 'New Project Name'})
        self.assertEqual(response.status_code, 403)

    def test_issue_author_can_edit_issue(self):
        data = {
            'name': 'New Issue Name',
            'description': 'New Description',
            'project': self.project.id,
            'author': self.user1.id
        }
        response = self.client.put(f'/api/issues/{self.issue.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_non_author_cannot_edit_comment(self):
        token = RefreshToken.for_user(self.user2)
        str_token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str_token}')
        data = {
            'description': 'New Comment',
            'issue': self.issue.id
        }
        response = self.client.put(f'/api/comments/{self.comment.id}/', data)
        self.assertEqual(response.status_code, 403)
