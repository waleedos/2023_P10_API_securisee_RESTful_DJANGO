from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import SignupAPIView
from .views import ProjectsViewset
from .views import ProjectsUsersViewset
from .views import IssueViewset
from .views import CommentViewset

router = routers.DefaultRouter()
router.register(r'projects', ProjectsViewset, basename='projects')
router.register(r'projects/(?P<project_id>[0-9]+)/users', ProjectsUsersViewset, basename='projects-users')
router.register(r'projects/(?P<project_id>[0-9]+)/issues', IssueViewset)
router.register(r'projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/comments', CommentViewset)

urlpatterns = [

    # JWT Users
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Import router urls
    path("", include(router.urls)),
    
]