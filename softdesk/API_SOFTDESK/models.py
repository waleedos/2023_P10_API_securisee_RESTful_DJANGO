from django.db import models  # Importe le module de modèles de Django
from django.contrib.auth.models import User  # Importe le modèle User de Django


# Définition du modèle "Project"
class Project(models.Model):

    # Déclare un tuple contenant les choix de types de projets
    TYPE = (
        ('PYTHON3', 'Python3'),
        ('DJANGO', 'Django'),
        ('REACT', 'React'),
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'IOS'),
        ('ANDROID', 'Android'),
    )

    # Déclare le champ pour le titre du projet
    title = models.CharField(max_length=255)
    # Déclare le champ pour la description du projet
    description = models.CharField(max_length=255)
    # Déclare le champ pour le type du projet
    type = models.CharField(max_length=255, choices=TYPE)
    # Création d'une relation de clé étrangère avec le modèle User pour l'auteur
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_author")
    # Création d'une relation ManyToMany pour les contributeurs via le modèle "Contributor"
    contributors = models.ManyToManyField(User, through="Contributor")

    # Méta-données pour ce modèle
    class Meta:
        verbose_name_plural = "Projects"

    # Représentation sous forme de chaîne de caractères du modèle
    def __str__(self):
        return self.title


# Définition du modèle "Contributor"
class Contributor(models.Model):

    # Déclare un tuple contenant les choix de permissions pour un contributeur
    PERMISSIONS = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    # Déclare le champ pour les permissions du contributeur
    permissions = models.CharField(max_length=255, choices=PERMISSIONS)
    # Déclare le champ pour le rôle du contributeur
    role = models.CharField(max_length=255, null=True, blank=True, default='')
    # Création d'une relation de clé étrangère avec le modèle User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Création d'une relation de clé étrangère avec le modèle Project
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    # Méta-données pour ce modèle
    class Meta:
        verbose_name_plural = "Contributors"

    # Représentation sous forme de chaîne de caractères du modèle
    def __str__(self):
        return self.user.username


# Définition du modèle "Issue"
class Issue(models.Model):

    # Déclare un tuple contenant les choix de priorités pour une "Issue"
    PRIORITY = (
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    )

    # Déclare un tuple contenant les choix de tags pour une "Issue"
    TAG = (
        ('BUG', 'Bug'),
        ('IMPROUVMENT', 'Improuvment'),
        ('TASK', 'Task'),
    )

    # Déclare un tuple contenant les choix de statuts pour une "Issue"
    STATUS = (
        ('TODO', 'Todo'),
        ('CURRENT', 'Current'),
        ('END', 'End'),
    )

    # Déclare le champ pour le titre de l'Issue
    title = models.CharField(max_length=255)
    # Déclare le champ pour la description de l'Issue
    desc = models.CharField(max_length=255)
    # Déclare le champ pour le tag de l'Issue
    tag = models.CharField(max_length=255, choices=TAG)
    # Déclare le champ pour la priorité de l'Issue
    priority = models.CharField(max_length=255, choices=PRIORITY)
    # Déclare le champ pour le statut de l'Issue
    status = models.CharField(max_length=255, choices=STATUS)
    # Déclare le champ pour la date de création de l'Issue
    created_time = models.DateTimeField(auto_now_add=True)
    # Création d'une relation de clé étrangère avec le modèle Project
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # Création d'une relation de clé étrangère avec le modèle User pour l'auteur
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Création d'une relation de clé étrangère avec le modèle User pour l'assigné
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_assignee')

    # Méta-données pour ce modèle
    class Meta:
        verbose_name_plural = "Issues"

    # Représentation sous forme de chaîne de caractères du modèle
    def __str__(self):
        return self.title


# Définition du modèle "Comment"
class Comment(models.Model):

    # Déclare le champ pour la description du commentaire
    description = models.CharField(max_length=255)
    # Déclare le champ pour la date de création du commentaire
    created_time = models.DateTimeField(auto_now=True)
    # Création d'une relation de clé étrangère avec le modèle User pour l'auteur
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Création d'une relation de clé étrangère avec le modèle Issue
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    # Méta-données pour ce modèle
    class Meta:
        verbose_name_plural = "Comments"

    # Représentation sous forme de chaîne de caractères du modèle
    def __str__(self):
        return self.description
