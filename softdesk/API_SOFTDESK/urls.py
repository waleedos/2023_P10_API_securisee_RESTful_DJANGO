# Importation des modules nécessaires de Django et Django REST Framework
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

# Importation des vues de l'application
from .views import SignupAPIView, ProjectsViewset, ProjectsUsersViewset, IssueViewset, CommentViewset

# Initialisation du routeur de Django REST Framework
router = routers.DefaultRouter()

# Enregistrement des vues sur le routeur
router.register(r'projects', ProjectsViewset, basename='projects')
router.register(r'projects/(?P<project_id>[0-9]+)/users', ProjectsUsersViewset, basename='projects-users')
router.register(r'projects/(?P<project_id>[0-9]+)/issues', IssueViewset)
router.register(r'projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/comments', CommentViewset)

# Définition des URL de l'application
urlpatterns = [

    # Route pour l'inscription des utilisateurs (JWT)
    path('signup/', SignupAPIView.as_view(), name='signup'),

    # Route pour l'obtention d'un token JWT (connexion)
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Importation des URL du routeur
    path("", include(router.urls)),
]
