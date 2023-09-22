from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Contributor, Project, Issue, Comment
from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsContributorOrReadOnly, IsIssueAuthorOrReadOnly, IsCommentAuthorOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrReadOnly]  # Ajout de IsAuthenticated

    @action(detail=True, methods=['POST'])
    def add_contributor(self, request, pk=None):
        project = self.get_object()
        username = request.data.get('username')
        user = User.objects.get(username=username)
        project.contributors.add(user)
        return Response({'status': 'Contributor added'})

    @action(detail=True, methods=['POST'])
    def remove_contributor(self, request, pk=None):
        project = self.get_object()
        username = request.data.get('username')
        user = User.objects.get(username=username)
        project.contributors.remove(user)
        return Response({'status': 'Contributor removed'})


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsIssueAuthorOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrReadOnly]
