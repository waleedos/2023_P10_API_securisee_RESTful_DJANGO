# Importation de BasePermission est importé pour créer une classe de permissions personnalisée.
from rest_framework.permissions import BasePermission

# Importation des modèles Project et Contributor
from .models import Project
from .models import Contributor
from django.shortcuts import get_object_or_404

# PERMISSION POUR L'ENDPOINT : Projet
#
# Endpoint :
#           /projects/
#           /projects/{id}
#
# 3. GET - Récupérer la liste de tous les projets associés à l'utilisateur connecté (filtré par queryset)
# 4. POST - Créer un projet (Tous les utilisateurs authentifiés)
# 5. GET - Récupérer les détails du projet à partir de son id (Auteur ou Contributeur)
# 6. PUT - Mettre à jour un projet (Auteur uniquement)
# 7. DELETE - Supprimer un projet et ses problèmes (Auteur uniquement)


# La classe PermissionProject hérite de BasePermission pour créer des règles de permissions personnalisées.
class PermissionProject(BasePermission):

    # Règle
    #
    # Un utilisateur authentifié peut créer un projet.
    # Un contributeur peut consulter le projet.
    # L'auteur peut effectuer toutes les opérations du contributeur.

    # Appel de cette methode pour vérifier les permissions au niveau de la requête, indépendamment des objets
    # spécifiques concernés. view.action est utilisé pour vérifier l'action qui est en cours de réalisation (list,
    # create, retrieve, update, destroy). return True indique que la permission est accordée pour cette action.
    def has_permission(self, request, view):
        user = request.user

        print("")
        print("# Permission_Project(has_permission) - Action : ", view.action, " User : ", user)

        # 3. GET - Récupérer la liste de tous les projets associés à l'utilisateur connecté
        if view.action == "list":
            print("# Action : List")
            print("# User is authenticated")
            print("# Return projects where user is a contributor or author. It is filtered by queryset")
            print("# Always authorized")
            return True

        # 4. POST - Créer un projet
        if view.action == "create":
            print("# Action : Create")
            print("# User is authenticated")
            print("# Authenticated user can create a project")
            return True

        # 5. GET - 5 - Récupérer les détails du projet à partir de son identifiant
        if view.action == "retrieve":
            print("# Action : Retrieve")
            print("# retrieve will be process in has_object_permission()")
            return True

        # 6. PUT - Mettre à jour un projet
        if view.action == "update":
            print("# Action : Update")
            print("# Update will be process in has_object_permission()")
            return True

        # 7. DELETE - Supprimer un projet et ses problèmes
        if view.action == "destroy":
            print("# Action : Destroy")
            print("# destroy will be process in has_object_permission()")
            return True

        # Finde cette classe de permissions
        print("# Permission_Project(has_permission) is finished")
        return True

    # Cette méthode est invoquée pour vérifier les permissions à l'échelle d'un objet donné. view.action est
    # utilisé comme précédemment, mais obj représente l'objet spécifique concerné. return True ou return False indique
    # si la permission est accordée ou non pour cet objet spécifique.
    def has_object_permission(self, request, view, obj):
        user = request.user

        print("")
        print(
            f"# Permission_Project(has_object_permission) : View action = {view.action}, User = {user}, "
            f"Object author = {obj.author}"
            )

        if view.action == "update" or view.action == "destroy":
            print("# Action : Update / Destroy")
            print("# Only project author is able to update/destroy a project")

            if (user == obj.author):
                print("# User is the author. Author is authorized")
                return True
            else:
                print("# User is not the project author : Not autorized")
                return False

        if view.action == "retrieve":
            print("# Action : Retrieve")
            print("# Author and contributor are able to retrieve a project")

            if (user == obj.author):
                print("# User is author. Author is authorized")
                return True

            if (user in obj.contributors.all()):
                print("# User is a contributor. Contributor is authorized")
                return True

            # Permission refusée = Permission denied
            print("# Not author, not contributor : Permission denied")
            return False

        print("# Permission_Project(has_object_permission) is finished")
        return True


# PERMISSION POUR POINT D'ACCÈS
#
# Endpoint :
#           /projects/{id}/users/
#           /projects/{id}/users/{id}
#
# 8.  POST - Ajouter un collaborateur à un projet (Auteur uniquement)
# 9.  GET - Récupérer la liste de tous les utilisateurs liés à un projet (Auteur ou Contributeur)
# 10. DELETE - Retirer un utilisateur d'un projet (Auteur uniquement)

# Définition de la classe PermissionProjectsUsers, qui hérite de BasePermission
class PermissionProjectsUsers(BasePermission):

    # Règle
    #
    # Un contributeur peut consulter la liste des contributeurs du projet.
    # L'auteur peut effectuer toutes les opérations du contributeur.

    # Méthode has_permission vérifie si un utilisateur a la permission de réaliser une action spécifique
    def has_permission(self, request, view):
        user = request.user  # Récupère l'utilisateur qui fait la requête

        # Affiche l'action et l'utilisateur pour des raisons de débogage
        print("# Permission_ProjectsUsers(has_permission) - Action : ", view.action, " User : ", user)

        # Vérification si l'action est 'list'
        if view.action == "list":
            print("# Action : List")  # Affiche l'action en cours
            # Affiche une note sur les utilisateurs qui peuvent réaliser cette action
            print("# Only project author or contributors are able to list users attached to a project")

            # Récupère l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')

            # Récupère le projet correspondant à cet ID ou retourne une erreur 404 si le projet n'existe pas
            project = get_object_or_404(Project, id=project_id)
            print("# Project_id : ", project_id)  # Affiche l'ID du projet

            # Vérifie si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# User is the project author : Author is authorized")
                return True  # Retourne True pour autoriser l'accès

            # Vérifie si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# L'utilisateur est un contributeur du projet : autorisé à lister")
                return True  # Retourne True pour autoriser l'accès

            # Si l'utilisateur n'est ni l'auteur ni un contributeur, il n'est pas autorisé à lister les utilisateurs
            print("# L'utilisateur n'est pas l'auteur ni un contributeur : non autorisé")  # Affiche un message de
            # débogage
            return False  # Retourne False pour refuser l'accès

        # Si l'action est 'create'
        if view.action == "create":
            print("# Action : Create")  # Affiche l'action en cours
            # Affiche une note sur les utilisateurs qui peuvent réaliser cette action
            print("# Seul l'auteur du projet peut ajouter un contributeur")

            # Récupère l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupère le projet correspondant à cet ID ou retourne une erreur 404 si le projet n'existe pas
            project = get_object_or_404(Project, id=project_id)
            print("# Project_id : ", project_id)  # Affiche l'ID du projet

            # Vérifie si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# L'utilisateur est l'auteur du projet : autorisé")  # Affiche un message de débogage
                return True  # Retourne True pour autoriser l'accès

            # Si l'utilisateur n'est pas l'auteur, il n'est pas autorisé à ajouter un contributeur
            print("# L'utilisateur n'est pas l'auteur du projet : non autorisé")  # Affiche un message de débogage
            return False  # Retourne False pour refuser l'accès

        # Si l'action est 'update'
        if view.action == "update":
            print("# Action : Update")  # Affiche l'action en cours
            # Affiche une note sur les utilisateurs qui peuvent réaliser cette action
            print("# Seul l'auteur du projet peut mettre à jour un contributeur")

            # Récupère l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupère le projet correspondant à cet ID ou retourne une erreur 404 si le projet n'existe pas
            project = get_object_or_404(Project, id=project_id)
            print("# Project_id : ", project_id)  # Affiche l'ID du projet

            # Vérifie si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# L'utilisateur est l'auteur du projet : autorisé")  # Affiche un message de débogage
                return True  # Retourne True pour autoriser l'accès

            # Si l'utilisateur n'est pas l'auteur, il n'est pas autorisé à mettre à jour un contributeur
            print("# L'utilisateur n'est pas l'auteur du projet : non autorisé")  # Affiche un message de débogage
            return False  # Retourne False pour refuser l'accès

        # Si l'action est 'destroy'
        if view.action == "destroy":
            print("# Action : Destroy")  # Affiche l'action en cours
            # Affiche une note sur les utilisateurs qui peuvent réaliser cette action
            print("# Seul l'auteur du projet peut supprimer un contributeur")

            # Récupère l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupère le projet correspondant à cet ID ou retourne une erreur 404 si le projet n'existe pas
            project = get_object_or_404(Project, id=project_id)
            print("# Project_id : ", project_id)  # Affiche l'ID du projet

            # Vérifie si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# L'utilisateur est l'auteur du projet : autorisé")  # Affiche un message de débogage
                return True  # Retourne True pour autoriser l'accès

            # Si l'utilisateur n'est pas l'auteur, il n'est pas autorisé à supprimer un contributeur
            print("# L'utilisateur n'est pas l'auteur du projet : non autorisé")  # Affiche un message de débogage
            return False  # Retourne False pour refuser l'accès

        # Si l'action est 'retrieve'
        if view.action == "retrieve":
            print("# Action : Retrieve")  # Affiche l'action en cours
            # Affiche une note sur les utilisateurs qui peuvent réaliser cette action
            print("# Seul l'auteur du projet ou les contributeurs peuvent "
                  "récupérer un utilisateur attaché à un projet")

            # Récupère l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupère le projet correspondant à cet ID ou retourne une erreur 404 si le projet n'existe pas
            project = get_object_or_404(Project, id=project_id)
            print("# Project_id : ", project_id)  # Affiche l'ID du projet

            # Vérifie si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# L'utilisateur est l'auteur du projet : autorisé")  # Affiche un message de débogage
                return True  # Retourne True pour autoriser l'accès

            # Vérifie si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# L'utilisateur est un contributeur du projet : "
                      "autorisé à lister")  # Affiche un message de débogage

                return True  # Retourne True pour autoriser l'accès

            # Si l'utilisateur n'est ni l'auteur ni un contributeur, il n'est pas autorisé
            print("# L'utilisateur n'est pas l'auteur et pas un contributeur, "
                  "non autorisé")  # Affiche un message de débogage

            return False  # Retourne False pour refuser l'accès

        # Le code pour vérifier les permissions est terminé
        print("# Permission_ProjectsUsers(has_permission) is finished")
        return True  # Retourne True par défaut

    # Définition de la méthode pour vérifier si l'utilisateur a la permission d'effectuer une action sur un objet
    def has_object_permission(self, request, view, obj):
        # Récupération de l'utilisateur courant à partir de la requête
        user = request.user

        # Affichage de diverses informations pour le débogage
        print(
            f"# Permission_ProjectsUsers(has_object_permission) : View action = {view.action}, User = {user}, "
            f"Object author = {obj.author}"
        )

        # Vérification si l'action à effectuer est de lister les objets
        if view.action == "list":
            print("Action : List")  # Affiche que l'action en cours est "list"

        # Vérification si l'action à effectuer est de créer un nouvel objet
        if view.action == "create":
            print("Action : Create")  # Affiche que l'action en cours est "create"

        # Vérification si l'action à effectuer est de mettre à jour un objet existant
        if view.action == "update":
            print("Action : Update")  # Affiche que l'action en cours est "update"

        # Vérification si l'action à effectuer est de supprimer un objet existant
        if view.action == "destroy":
            print("Action : Destroy")  # Affiche que l'action en cours est "destroy"

        # Vérification si l'action à effectuer est de récupérer les détails d'un objet
        if view.action == "retrieve":
            print("Action : Retrieve")  # Affiche que l'action en cours est "retrieve"

        # Message pour indiquer que la vérification des permissions est terminée
        print("# Permission_ProjectsUsers(has_object_permission) is finished")

        # Retourne True pour indiquer que l'utilisateur a la permission
        return True


# PERMISSION POUR POINT D'ACCÈS
#
# Endpoint :
#           /projects/{id}/issues/
#           /projects/{id}/issues/{id}
#
# 11. GET - Récupérer la liste des problèmes liés à un projet (Uniquement le contributeur)
# 12. POST - Créer un problème dans un projet (Contributeur)
# 13. PUT - Mettre à jour un problème dans un projet (Uniquement l'auteur)
# 14. DELETE - Supprimer un problème d'un projet (Uniquement l'auteur)

class PermissionIssue(BasePermission):

    # Règle
    #
    # Un contributeur peut créer et consulter un problème
    # L'auteur du projet peut créer et consulter un problème
    # L'auteur du problème peut lire, mettre à jour et supprimer le problème

    # Définition de la méthode pour vérifier si l'utilisateur a la permission générale pour une action donnée
    def has_permission(self, request, view):
        # Récupération de l'utilisateur courant à partir de la requête
        user = request.user

        # Affichage des informations sur l'action et l'utilisateur pour le débogage
        print("# Permission_Issue(has_permission) - Action : ", view.action, " User : ", user)

        # Vérification si l'action est de lister les 'issues'
        if view.action == "list":
            print("# Action : List")
            print("# Project author or contributor are able to read the issue")

            # Récupération de l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupération de l'objet Project correspondant à l'ID
            project = get_object_or_404(Project, id=project_id)

            # Affichage de l'ID du projet pour le débogage
            print("# Project_id :", project_id)

            # Vérification si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# User is the project author. Project author is authorized")
                return True  # Autorisation accordée

            # Vérification si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor : Contributor is authorized to list")
                return True  # Autorisation accordée

            # Si l'utilisateur n'est ni l'auteur ni un contributeur
            print("# User is a not a project contributor : User is not authorized to list")
            return False  # Autorisation refusée

        # Vérification si l'action est de créer un nouvel 'issue'
        if view.action == "create":
            print("# Action : Create")
            print("# Project author or contributors only can create issue")

            # Récupération de l'ID du projet depuis les arguments de la vue
            project_id = view.kwargs.get('project_id')
            # Récupération de l'objet Project correspondant à l'ID
            project = get_object_or_404(Project, id=project_id)

            # Affichage de l'ID du projet pour le débogage
            print("Project_id :", project_id)

            # Vérification si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("User is the project author. Project author is autorized")
                return True  # Autorisation accordée

            # Vérification si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor : Contributor is authorized to create")
                return True  # Autorisation accordée

            # Si l'utilisateur n'est ni l'auteur ni un contributeur
            print("# User is a not a project contributor : User is not authorized to create")
            return False  # Autorisation refusée

        # Vérification si l'action est de mettre à jour un 'issue'
        if view.action == "update":
            print("# Action : Update")

        # Vérification si l'action est de détruire un 'issue'
        if view.action == "destroy":
            print("# Action : Destroy")

        # Vérification si l'action est de récupérer un 'issue'
        if view.action == "retrieve":
            print("# Action : Retrieve")

        # Message indiquant que la méthode has_permission est terminée
        print("# Permission_Issue(has_permission) is finished")
        return True  # Autorisation accordée par défaut

    # Définition de la méthode has_object_permission pour gérer les permissions d'objet
    def has_object_permission(self, request, view, obj):
        # Récupération de l'utilisateur à partir de la requête
        user = request.user

        # Affichage des informations de débogage
        print(
            f"# Permission_Issue(has_object_permission) : View action = {view.action}, User = {user}, "
            f"Object author = {obj.author}"
        )

        # Vérification si l'action est de lister les 'issues'
        if view.action == "list":
            print("# Action : List")

        # Vérification si l'action est de créer un 'issue'
        if view.action == "create":
            print("# Action : Create")

        # Vérification si l'action est de mettre à jour un 'issue'
        if view.action == "update":
            print("# Action : Update")
            print("# Only issue's author can update the issue")

            # Autorisation si l'utilisateur est l'auteur de l'issue
            if user == obj.author:
                print("# User is the issue author. User is authorized")
                return True
            else:
                print("# User is not the issue author. User is unauthorized")
                return False

        # Vérification si l'action est de détruire un 'issue'
        if view.action == "destroy":
            print("# Action : Destroy")
            print("# Only issue's author can delete the issue")

            # Autorisation si l'utilisateur est l'auteur de l'issue
            if user == obj.author:
                print("# User is the issue author. User is authorized")
                return True
            else:
                print("# User is not the issue author. User is unauthorized")
                return False

        # Vérification si l'action est de récupérer un 'issue'
        if view.action == "retrieve":
            print("# Action : Retrieve")
            print("# Project author, contributors or issue's author can retrieve")

            # Récupération de l'ID du projet
            project_id = view.kwargs.get('project_id')
            # Récupération du projet associé à cet ID
            project = get_object_or_404(Project, id=project_id)

            print("# Project_id :", project_id)

            # Autorisation si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# User is the project author. User is authorized")
                return True

            # Autorisation si l'utilisateur est l'auteur de l'issue
            if user == obj.author:
                print("# User is the issue author. User is authorized")
                return True

            # Autorisation si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor. User is authorized")
                return True

            print("# User is not Project author, contributor or issue author. User is not authorized")
            return False

        # Message indiquant que la méthode has_object_permission est terminée
        print("# Permission_Issue(has_object_permission) is finished")
        return True  # Autorisation accordée par défaut


# PERMISSION POUR LE POINT D'ACCÈS
#
# Endpoints :
#           /projects/{id}/issues/{id}/comments/
#           /projects/{id}/issues/{id}/comments/{id}
#
# 15. POST - Créer des commentaires sur un problème (Auteur ou Contributeur)
# 16. GET - Récupérer la liste de tous les commentaires liés à un problème (Auteur ou Contributeur)
# 17. PUT - Éditer un commentaire (Auteur uniquement)
# 18. DELETE - Supprimer un commentaire (Auteur uniquement)
# 19. GET - Obtenir un commentaire via son identifiant (Auteur ou Contributeur)

class PermissionComment(BasePermission):

    # Règle
    #
    # Un contributeur peut créer et consulter des commentaires
    # L'auteur du projet peut créer et consulter des commentaires
    # L'auteur d'un commentaire peut lire, mettre à jour et supprimer le commentaire

    # Définition de la méthode has_permission pour gérer les permissions globales
    def has_permission(self, request, view):
        # Récupération de l'utilisateur à partir de la requête
        user = request.user

        # Affichage des informations de débogage
        print("# Permission_Comment(has_permission) - Action : ", view.action, " User : ", user)

        # Vérification si l'action est de lister les commentaires
        if view.action == "list":
            print("# Action : List")
            print("# Only project contributors or project author can list comments")

            # Récupération de l'ID du projet
            project_id = view.kwargs.get('project_id')
            # Récupération du projet associé à cet ID
            project = get_object_or_404(Project, id=project_id)

            print("# Project_id :", project_id)

            # Autorisation si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("User is the project author. User is authorized")
                return True

            # Autorisation si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor. User is authorized")
                return True
            else:
                print("# User is a not a project contributor. User is not authorized ")
                return False

        # Vérification si l'action est de créer un commentaire
        if view.action == "create":
            print("# Action : Create")
            print("# Only project contributors or project author can create comments")

            # Récupération de l'ID du projet
            project_id = view.kwargs.get('project_id')
            # Récupération du projet associé à cet ID
            project = get_object_or_404(Project, id=project_id)

            print("# Project_id :", project_id)

            # Autorisation si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("User is the project author. User is authorized")
                return True

            # Autorisation si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor. User is authorized")
                return True
            else:
                print("# User is a not a project contributor. User is not authorized")
                return False

        # Vérification si l'action est de mettre à jour un commentaire
        if view.action == "update":
            print("# Action : Update")

        # Vérification si l'action est de détruire un commentaire
        if view.action == "destroy":
            print("# Action : Destroy")

        # Vérification si l'action est de récupérer un commentaire
        if view.action == "retrieve":
            print("# Action : Retrieve")

        # Message indiquant que la méthode has_permission est terminée
        print("# Permission_Comment(has_permission) is finished")
        return True  # Autorisation accordée par défaut

    # Définition de la méthode has_object_permission pour gérer les permissions sur un objet spécifique
    def has_object_permission(self, request, view, obj):
        # Récupération de l'utilisateur à partir de la requête
        user = request.user

        # Affichage des informations de débogage
        print(
            f"# Permission_Comment(has_object_permission) : View action = {view.action}, User = {user}, "
            f"Object author = {obj.author}"
            )

        # Vérification si l'action est de lister les commentaires
        if view.action == "list":
            print("# Action : List")

        # Vérification si l'action est de créer un commentaire
        if view.action == "create":
            print("# Action : Create")

        # Vérification si l'action est de mettre à jour un commentaire
        if view.action == "update":
            print("# Action : Update")
            print("# Only comment's author can update comment")

            # Autorisation si l'utilisateur est l'auteur du commentaire
            if user == obj.author:
                print("# User is the comment's author. User is authorized")
                return True
            else:
                print("# User is not the comment's author. User is not authorized")
                return False

        # Vérification si l'action est de détruire un commentaire
        if view.action == "destroy":
            print("# Action : Destroy")
            print("# Only comment's author can delete comment")

            # Autorisation si l'utilisateur est l'auteur du commentaire
            if user == obj.author:
                print("# User is the comment's author. User is authorized")
                return True
            else:
                print("# User is not the comment's author. User is not authorized")
                return False

        # Vérification si l'action est de récupérer un commentaire
        if view.action == "retrieve":
            print("# Action : Retrieve")
            print("# Only project contributors can read comments")

            # Récupération de l'ID du projet
            project_id = view.kwargs.get('project_id')
            # Récupération du projet associé à cet ID
            project = get_object_or_404(Project, id=project_id)

            print("# Project id :", project_id)

            # Autorisation si l'utilisateur est l'auteur du projet
            if user == project.author:
                print("# User is the project author. User is authorized")
                return True

            # Autorisation si l'utilisateur est l'auteur du commentaire
            if user == obj.author:
                print("# User is the comment's author. User is authorized")
                return True

            # Autorisation si l'utilisateur est un contributeur du projet
            if Contributor.objects.filter(user=user, project=project).exists():
                print("# User is a project contributor. User is authorized.")
                return True
            else:
                print("# User is a not a project contributor. User is not authorized")
                return False

        # Message indiquant que la méthode has_object_permission est terminée
        print("# Permission_Comment(has_object_permission) is finished")
        return True  # Autorisation accordée par défaut
