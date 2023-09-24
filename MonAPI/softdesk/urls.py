from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import UserProfileView, UserDeleteView
from .views import UserDataExportView


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contributors', views.ContributorViewSet)
router.register(r'issues', views.IssueViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'projects', views.ProjectViewSet)

# Pas besoin de project_router ici, utilisez simplement router

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('profile/export/', UserDataExportView.as_view(), name='user-data-export'),
]
