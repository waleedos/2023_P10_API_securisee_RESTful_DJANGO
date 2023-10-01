# Importation des modules nécessaires pour les vues et les permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# Importation des modèles et des serializers personnalisés
from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment
from .serializers import SignupSerializer
from .serializers import ProjectSerializer
from .serializers import ContributorSerializer
from .serializers import IssueSerializer
from .serializers import CommentSerializer

# Importation des permissions personnalisées
from .permissions import PermissionProject
from .permissions import PermissionProjectsUsers
from .permissions import PermissionIssue
from .permissions import PermissionComment


# Vue pour l'enregistrement des utilisateurs
# 1. Enregistrement de l'utilisateur - POST - /signup/
class SignupAPIView(APIView):

    # Définir le serializer et les permissions pour cette vue
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    # Méthode POST pour créer un nouvel utilisateur
    def post(self, request):
        # Récupération des données envoyées dans la requête
        user = request.data
        # Initialisation du serializer avec ces données
        serializer = SignupSerializer(data=user)

        # Vérification de la validité des données
        if serializer.is_valid():
            # Enregistrement du nouvel utilisateur dans la base de données
            serializer.save()
            # Renvoie une réponse HTTP 201 avec les données de l'utilisateur
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # En cas d'erreur de validation, renvoie une réponse HTTP 400
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# 2. Connexion - POST - /login/

# Endpoint :
#           /projets/
#           /projets/{id}
#
# 3. GET - Récupérer la liste de tous les projets liés à l'utilisateur connecté
# 4. POST - Créer un projet
# 5. GET - Récupérer les détails d'un projet à partir de son ID
# 6. PUT - Mettre à jour un projet
# 7. DELETE - Supprimer un projet et ses problèmes


# Classe pour les opérations CRUD sur les projets
class ProjectsViewset(ModelViewSet):

    # Spécifier le serializer et les classes de permission pour cette vue
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, PermissionProject]

    # 3. GET - Récupérer la liste de tous les projets associés à l'utilisateur connecté
    def get_queryset(self):
        print("#################################################")
        print("# Views.py : ProjectsViewset: get()")
        print("# L'utilisateur doit être authentifié.")
        print("# Classe de permission limitée : PermissionProject")

        # Récupération de l'utilisateur connecté
        user = self.request.user

        # Si un 'pk' est présent, il faut récupérer tous les résultats pour que les permissions puissent être
        # appliquées et ne pas retourner "non trouvé"
        pk = self.kwargs.get('pk')

        if pk is None:
            print("# Les résultats sont filtrés : "
                  "Affichage uniquement des projets où l'utilisateur est auteur ou contributeur")
            queryset = (Project.objects.filter(contributors=user) |
                        Project.objects.filter(author=user))

        else:
            print("# Les résultats ne sont pas filtrés. Permet d'appliquer la permission sur un seul objet.")
            queryset = Project.objects.all()

        return queryset

    # 4. POST - Créer un projet
    def create(self, request, *args, **kwargs):
        print("# ProjectsViewset: create()")

        # Initialisation du serializer avec les données de la requête
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Valide les données et lève une exception si elles ne sont pas
        # valides
        serializer.validated_data['author'] = request.user  # Attribue l'utilisateur connecté comme auteur du projet

        serializer.save()  # Sauvegarde l'instance du projet
        headers = self.get_success_headers(serializer.data)  # Récupère les en-têtes de la réponse réussie
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 5. GET - Récupérer les détails d'un projet à partir de son id
    def retrieve(self, request, *args, **kwargs):
        print("# ProjectsViewset: retrieve()")

        # Récupère l'id du projet depuis les arguments de la requête
        project_id = self.kwargs.get('pk')
        print("# ProjectsViewset: retrieve(", project_id, ")")

        # Récupère l'instance du projet
        instance = self.get_object()

        # Utilisation du serializer pour transformer l'objet en JSON
        serializer = self.get_serializer(instance)

        # Retourne une réponse avec les données sérialisées
        return Response(serializer.data)

    # 6. PUT - Mettre à jour un projet
    def update(self, request, *args, **kwargs):
        print("# ProjectsViewset: update()")

        # Vérifie si la mise à jour doit être partielle (true si on utilise PATCH)
        partial = kwargs.pop('partial', False)

        # Récupère l'instance du projet à mettre à jour
        instance = self.get_object()

        # Initialise le serializer avec les données de la requête et l'instance à mettre à jour
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        # Valide les données et lève une exception en cas d'erreur
        serializer.is_valid(raise_exception=True)

        # Sauvegarde les modifications apportées à l'instance
        serializer.save()

        # Retourne une réponse avec les données sérialisées du projet mis à jour
        return Response(serializer.data)

    # 7. DELETE - Supprimer un projet et ses problèmes associés
    def destroy(self, request, *args, **kwargs):
        print("# ProjectsViewset: destroy()")

        # Récupère l'instance du projet à supprimer
        instance = self.get_object()

        # Supprime l'instance du projet
        instance.delete()

        # Retourne une réponse HTTP 204 indiquant que la ressource a été supprimée avec succès
        return Response(status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projets/{id}/utilisateurs/
#           /projets/{id}/utilisateurs/{id}
#
# 8.  POST - Ajouter un collaborateur à un projet
# 9.  GET - Récupérer la liste de tous les utilisateurs associés à un projet
# 10. DELETE - Retirer un utilisateur d'un projet


# Classe pour gérer les vues associées aux collaborateurs d'un projet
class ProjectsUsersViewset(ModelViewSet):

    # Spécifie le serializer à utiliser
    serializer_class = ContributorSerializer

    # Définit les permissions nécessaires
    permission_classes = [IsAuthenticated, PermissionProjectsUsers]

    # Récupère tous les collaborateurs
    def get_queryset(self):
        queryset = Contributor.objects.all()
        return queryset

    # 8. POST - Ajoute un collaborateur à un projet
    def create(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset: create()")

        # Récupère l'ID du projet depuis les arguments de l'URL
        project_id = self.kwargs.get('project_id')

        # Récupère les données nécessaires à partir du corps de la requête
        user_id = request.data.get('user_id')
        permissions = request.data.get('permissions')
        role = request.data.get('role')

        # Obtient les objets du projet et de l'utilisateur
        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        # Crée un nouvel objet Contributor
        contributor = Contributor(project=project, user=user, permissions=permissions, role=role)
        contributor.save()

        # Sérialise et retourne le nouvel objet Contributor
        serializer = ContributorSerializer(contributor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 9. GET - Récupère la liste de tous les utilisateurs liés à un projet
    def list(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset: list()")

        # Récupère l'ID du projet depuis les arguments de l'URL
        project_id = self.kwargs.get('project_id')

        # Filtrer les objets Contributor en fonction de l'ID du projet
        contributors = Contributor.objects.filter(project_id=project_id)

        # Sérialise et retourne les objets Contributor
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 10. DELETE - Supprime un utilisateur d'un projet
    def destroy(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset : destroy()")

        # Récupère l'ID de l'utilisateur et du projet depuis les arguments de l'URL
        user_id = self.kwargs.get('pk')
        project_id = self.kwargs.get('project_id')

        # Obtient les objets du projet et de l'utilisateur
        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        # Trouve et supprime le collaborateur
        contributor = Contributor.objects.filter(project=project, user=user)
        contributor.delete()

        # Retourne une réponse HTTP 204
        return Response("", status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projets/{id}/problèmes/
#           /projets/{id}/problèmes/{id}
#
# 11. GET - Récupérer la liste des problèmes liés à un projet
# 12. POST - Créer un problème dans un projet
# 13. PUT - Mettre à jour un problème dans un projet
# 14. DELETE - Supprimer un problème d'un projet

# Classe pour gérer les vues associées aux problèmes (Issues) d'un projet
class IssueViewset(ModelViewSet):

    # Définit les objets et le serializer
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    # Définit les permissions
    permission_classes = [IsAuthenticated, PermissionIssue]

    # 11. GET - Récupère la liste des problèmes liés à un projet
    def get_queryset(self):
        print("# IssueViewset: get()")

        # Récupère l'ID du projet depuis les arguments de l'URL
        project_id = self.kwargs.get('project_id')

        # Filtre les problèmes en fonction de l'ID du projet
        queryset = Issue.objects.filter(project_id=project_id)
        return queryset

    # 12. POST - Crée un problème dans un projet
    def create(self, request, *args, **kwargs):
        print("# IssueViewset: create()")

        # Vérifie les permissions
        self.check_permissions(request)

        # Récupère l'ID du projet et l'objet projet correspondant
        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)

        # Valide les données envoyées
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Ajoute le projet et l'utilisateur assigné aux données validées
        serializer.validated_data['project'] = project
        serializer.validated_data['assignee'] = request.user

        # Crée le nouvel objet Issue
        self.perform_create(serializer)

        # Retourne une réponse HTTP 201 avec les données du nouvel objet
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 13. PUT - Met à jour un problème dans un projet
    def update(self, request, *args, **kwargs):
        print("# IssueViewset: update()")

        # Récupère l'objet Issue à mettre à jour
        instance = self.get_object()

        # Met à jour l'objet avec les nouvelles données
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Retourne une réponse avec les données mises à jour
        return Response(serializer.data)

    # 14. DELETE - Supprime un problème d'un projet
    def destroy(self, request, *args, **kwargs):
        print("# IssueViewset: destroy()")

        # Récupère l'objet Issue à supprimer
        instance = self.get_object()

        # Supprime l'objet
        self.perform_destroy(instance)

        # Retourne une réponse HTTP 204 pour indiquer la suppression réussie
        return Response(status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projets/{id}/problèmes/{id}/commentaires/
#           /projets/{id}/problèmes/{id}/commentaires/{id}
#
# 15. POST - Créer des commentaires sur un problème
# 16. GET - Récupérer la liste de tous les commentaires liés à un problème
# 17. PUT - Éditer un commentaire
# 18. DELETE - Supprimer un commentaire
# 19. GET - Obtenir un commentaire via son identifiant


# Classe pour gérer les vues associées aux commentaires d'un problème (Issue)
class CommentViewset(ModelViewSet):

    # Définit les objets et le serializer
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # Définit les permissions
    permission_classes = [IsAuthenticated, PermissionComment]

    # 15. POST - Créer des commentaires sur un problème
    def create(self, request, *args, **kwargs):
        print("# CommentViewset: create()")

        # Récupère les IDs du projet et du problème depuis les arguments de l'URL
        project_id = self.kwargs['project_id']
        issue_id = self.kwargs['issue_id']

        print("Project_id:", project_id, ", Issue_id:", issue_id)

        # Valide les données envoyées
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Récupère le problème correspondant aux IDs
        issue = Issue.objects.get(id=issue_id, project_id=project_id)

        # Ajoute le problème aux données validées
        serializer.validated_data['issue'] = issue

        # Crée le nouveau commentaire
        self.perform_create(serializer)

        # Retourne une réponse HTTP 201 avec les données du nouveau commentaire
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 16. GET - Récupère la liste de tous les commentaires liés à un problème
    def get_queryset(self):
        print("# CommentViewset: get()")

        # Récupère les IDs du projet, du problème et du commentaire depuis les arguments de l'URL
        project_id = self.kwargs['project_id']
        issue_id = self.kwargs['issue_id']
        comment_id = self.kwargs.get('pk')

        # Vérifie si un 'comment_id' est fourni
        if comment_id is None:

            print("# Results are filtered by project_id and issue_id.")
            # Filtre les commentaires en fonction des IDs du projet et du problème
            queryset = Comment.objects.filter(issue__project_id=project_id, issue_id=issue_id)
        else:
            print("No filter because 'comment_id' is set.")
            # Ne filtre pas les résultats si 'comment_id' est fourni
            queryset = Comment.objects.all()

        return queryset

    # 17. PUT - Modifier un commentaire
    def update(self, request, *args, **kwargs):
        print("# CommentViewset: update()")

        # Obtient l'objet Comment à partir de la base de données
        instance = self.get_object()

        # Initialise le serializer avec les données existantes et les nouvelles données
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        # Vérifie si les données sont valides
        serializer.is_valid(raise_exception=True)

        # Effectue la mise à jour de l'objet Comment
        self.perform_update(serializer)

        # Retourne une réponse HTTP avec les données mises à jour
        return Response(serializer.data)

    # 18. DELETE - Supprimer un commentaire
    def destroy(self, request, *args, **kwargs):
        print("# CommentViewset: destroy()")

        # Obtient l'objet Comment à partir de la base de données
        instance = self.get_object()

        # Supprime l'objet Comment
        self.perform_destroy(instance)

        # Retourne une réponse HTTP 204 indiquant que la suppression a été réussie
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 19. GET - Obtenir un commentaire via son ID
    def retrieve(self, request, *args, **kwargs):
        print("# CommentViewset: retrieve()")

        # Obtient l'objet Comment à partir de la base de données
        instance = self.get_object()

        # Initialise le serializer avec l'objet Comment
        serializer = self.get_serializer(instance)

        # Retourne une réponse HTTP avec les données du commentaire
        return Response(serializer.data)
