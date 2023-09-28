from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Nécessaire pour la conformité RGPD, vérifie si l'utilisateur a plus de 15 ans
    age = models.IntegerField()

    # Pour savoir si l'utilisateur souhaite être contacté
    can_be_contacted = models.BooleanField(default=False)

    # Pour savoir si l'utilisateur permet le partage de ses données
    can_data_be_shared = models.BooleanField(default=False)

    # Nouveau champ pour le consentement
    consent = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
        # Utilise la même table que le modèle User intégré


class Contributor(models.Model):
    # Clé étrangère vers le modèle User, indique quel utilisateur est un contributeur
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Clé étrangère vers le modèle Project, indique à quel projet l'utilisateur contribue
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


class Project(models.Model):
    # Nom du projet
    name = models.CharField(max_length=255)

    # Description du projet
    description = models.TextField()

    # Type du projet (back-end, front-end, iOS, Android)
    type = models.CharField(max_length=50)

    # Auteur du projet
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_projects')

    # Liste des contributeurs du projet
    contributors = models.ManyToManyField(User, through='Contributor', related_name='contributed_to_projects')


class Issue(models.Model):
    # Nom de l'issue (tâche ou problème)
    name = models.CharField(max_length=255)

    # Description de l'issue
    description = models.TextField()

    # Projet associé à l'issue
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Auteur de l'issue
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    # Description du commentaire
    description = models.TextField()

    # Issue associée au commentaire
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    # Auteur du commentaire
    author = models.ForeignKey(User, on_delete=models.CASCADE)
