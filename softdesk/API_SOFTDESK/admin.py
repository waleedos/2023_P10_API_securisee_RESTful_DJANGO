from django.contrib import admin
# import du module admin de Django. C'est le module qui fournit toutes les fonctionnalités nécessaires pour créer une
# interface d'administration.

# from django.contrib.auth.admin import UserAdmin
# Import la classe UserAdmin du module django.contrib.auth.admin. Cette classe fournit une interface d'administration
# pour les utilisateurs.

from django.contrib.auth.models import User
# Import de la classe User qui est le modèle d'utilisateur par défaut de Django.

from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment
# Import de mes propres modèles (Project, Contributor, Issue, Comment) que vous avez définis dans le fichier models.py.


# Manage ManytoMany in django administration interface
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models
#

class ContributorsInline(admin.TabularInline):
    model = Contributor
    extra = 1
# La classe ContributorsInline permet d'afficher les instances du modèle Contributor dans le même formulaire que les
# modèles auxquels il est lié (dans ce cas, User et Project). Le paramètre extra = 1 signifie qu'un formulaire vide
# sera affiché, permettant de créer une nouvelle instance de Contributor directement.


class UserAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]
    readonly_fields = ('id', )
# Cette classe UserAdmin étend admin.ModelAdmin et personnalise l'affichage du modèle User dans l'interface
# d'administration. inlines = [ContributorsInline] ajoute les instances du modèle Contributor associées à un User.
# Le champ id est rendu en lecture seule (readonly_fields).


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'id',)
# Cette classe IssueAdmin rend les champs created_time et id en lecture seule dans l'interface d'administration.


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'id',)
# Cette classe CommentAdmin fait de même pour le modèle Comment.


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]
    readonly_fields = ('id', )
# La classe ProjectAdmin rend le champ id en lecture seule et ajoute les instances du modèle Contributor associées à
# un Project.

# -------------------------------------------------------------
# Enregistrement des modèles dans l'interface d'administration
# -------------------------------------------------------------


admin.site.unregister(User)
# Cette ligne désenregistre le modèle User par défaut pour permettre de l'enregistrer à nouveau avec la nouvelle
# classe UserAdmin.


admin.site.register(User, UserAdmin)
# Enregistrement du modèle User avec la classe UserAdmin que vous avez définie.

admin.site.register(Contributor)
# Enregistrement du modèle Contributor.

admin.site.register(Project, ProjectAdmin)
# Enregistrement du modèle Project avec la classe ProjectAdmin que vous avez définie.

admin.site.register(Issue, IssueAdmin)
# Enregistrement du modèle Issue avec la classe IssueAdmin que vous avez définie.

admin.site.register(Comment, CommentAdmin)
# Enregistrement le modèle Comment avec la classe CommentAdmin que vous avez définie.
