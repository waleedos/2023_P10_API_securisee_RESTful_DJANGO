from django.http import JsonResponse
from django.views.decorators.cache import cache_page  # Import pour la mise en cache
from rest_framework import viewsets, generics, permissions, serializers
from rest_framework.permissions import IsAuthenticated
from .models import User, Contributor, Project, Issue, Comment
from .serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsContributorOrReadOnly, IsIssueAuthorOrReadOnly, IsCommentAuthorOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Prefetch


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        user.consent = self.request.data.get('consent', False)
        age = self.request.data.get('age', 0)
        if int(age) < 15:
            raise serializers.ValidationError("Vous devez avoir au moins 15 ans pour vous inscrire.")
        user.save()


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related('author').prefetch_related(
        Prefetch('contributors', queryset=Contributor.objects.select_related('user'))
    )
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsContributorOrReadOnly]

    @cache_page(60 * 15)  # Cache pendant 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

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


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDataExportView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        data = {
            "username": user.username,
            "email": user.email,
        }
        return JsonResponse(data)
