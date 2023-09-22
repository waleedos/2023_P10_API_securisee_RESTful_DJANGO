from rest_framework import permissions
from .models import Contributor  # Importez seulement les modèles nécessaires


class IsContributorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return Contributor.objects.filter(
            user=request.user, project=obj
        ).exists()


class IsIssueAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# Nouvelle classe de permission
# J'ai laissé cette classe vide car vous n'avez pas spécifié de logique de permission pour elle.
class AnotherPermissionClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Votre logique de permission ici
        pass
