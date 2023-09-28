from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment

from .serializers import SignupSerializer
from .serializers import ProjectSerializer
from .serializers import ContributorSerializer
from .serializers import IssueSerializer
from .serializers import CommentSerializer

from .permissions import PermissionProject
from .permissions import PermissionProjectsUsers
from .permissions import PermissionIssue
from .permissions import PermissionComment


#
# 1. User registration - POST - /signup/
#
class SignupAPIView(APIView):  
    
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = SignupSerializer(data=user)

        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=status.HTTP_201_CREATED )

        return Response( { "Errors" : serializer.errors }, status=status.HTTP_400_BAD_REQUEST )


#
# 2. Login - POST - /login/
#
# TokenObtainPairView


# ModelViewSet
#
# Endpoint :
#           /projects/
#           /projects/{id}
#
# 3. GET - Retrieve the list of all the projects attached to the connected user
# 4. POST - Create a project
# 5. GET - Retrieve project details from its id
# 6. PUT - Update a project
# 7. DELETE - Delete a project and its problems
#
class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, PermissionProject]
    
    # 3. GET - Retrieve the list of all the projects attached to the connected user
    def get_queryset(self):
        print("#################################################")
        print("# Views.py : ProjectsViewset: get()")
        print("# User must be authentificated.")
        print("# Permission class limitation : PermissionProject")

        user = self.request.user

        # If there is a 'pk', you must retrieve all the results so that the permissions can be applied and not return "not found"
        pk = self.kwargs.get('pk')
        
        if (pk == None ):
            print("# Results are filtered : Display only projects where the user is author or contributor")
            queryset = Project.objects.filter(contributors=user) | Project.objects.filter(author=user)
        else:
            print("# Results are not filtered. Allow permission to be apply on one object.")
            queryset = Project.objects.all()

        return queryset

    # 4. POST - Create a project
    def create(self, request, *args, **kwargs):
        print("# ProjectsViewset: create()")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = request.user
        
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 5. GET - Retrieve project details from its id
    def retrieve(self, request, *args, **kwargs):
        print("# ProjectsViewset: retrieve()")

        project_id = self.kwargs.get('pk')
        print("# ProjectsViewset: retrieve(", project_id, ")")
              
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    # 6. PUT - Update a project
    def update(self, request, *args, **kwargs):
        print("# ProjectsViewset: update()")

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # 7. DELETE - Delete a project and its problems
    def destroy(self, request, *args, **kwargs):
        print("# ProjectsViewset: destroy()")

        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projects/{id}/users/
#           /projects/{id}/users/{id}
#
# 8.  POST - Add a collaborator to a project
# 9.  GET - Retrieve the list of all users attached to a project
# 10. DELETE - Remove a user from a project
#
class ProjectsUsersViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, PermissionProjectsUsers]

    def get_queryset(self):
        queryset = Contributor.objects.all()
        return queryset


    # 8.  POST - Add a collaborator to a project
    def create(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset: create()")

        project_id = self.kwargs.get('project_id')

        user_id = request.data.get('user_id')
        permissions = request.data.get('permissions')
        role = request.data.get('role')
     
        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        contributor = Contributor(project=project, user=user, permissions=permissions, role=role)
        contributor.save()

        serializer = ContributorSerializer(contributor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 9.  GET - Retrieve the list of all users attached to a project 
    def list(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset: list()")

        project_id = self.kwargs.get('project_id')

        contributors = Contributor.objects.filter(project_id=project_id)

        serializer = ContributorSerializer(contributors, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 10. DELETE - Remove a user from a project
    def destroy(self, request, *args, **kwargs):
        print("# ProjectsUsersViewset : destroy()")

        user_id = self.kwargs.get('pk')
        project_id = self.kwargs.get('project_id') 

        project = Project.objects.get(id=project_id)
        user = User.objects.get(id=user_id)

        contributor = Contributor.objects.filter(project=project, user=user)
        contributor.delete()

        return Response("", status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projects/{id}/issues/
#           /projects/{id}/issues/{id}
#
# 11. GET - Retrieve the list of problems related to a project
# 12. POST - Creating a problem in a project
# 13. PUT - Update a problem in a project
# 14. DELETE - Delete a problem from a project
#
class IssueViewset(ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, PermissionIssue]

    # 11. GET - Retrieve the list of problems related to a project
    def get_queryset(self):
        print("# IssueViewset: get()")

        project_id = self.kwargs.get('project_id')
        queryset = Issue.objects.filter(project_id=project_id)
        return queryset

    # 12. POST - Creating a problem in a project
    def create(self, request, *args, **kwargs):      
        print("# IssueViewset: create()")

        self.check_permissions(request) 

        project_id = self.kwargs.get('project_id')
        project = Project.objects.get(id=project_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['project'] = project
        serializer.validated_data['assignee'] = request.user

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 13. PUT - Update a problem in a project
    def update(self, request, *args, **kwargs):
        print("# IssueViewset: update()")

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    # 14. DELETE - Delete a problem from a project
    def destroy(self, request, *args, **kwargs):
        print("# IssueViewset: destroy()")
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# ModelViewSet
#
# Endpoint :
#           /projects/{id}/issues/{id}/comments/
#           /projects/{id}/issues/{id}/comments/{id}
#
# 15. POST - Create comments on a problem
# 16. GET - Retrieve the list of all comments related to a problem
# 17. PUT -  Edit a comment
# 18. DELETE - Delete a comment
# 19. GET - Get a comment via its id
#
class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, PermissionComment]


    # 15. POST - Create comments on a problem
    def create(self, request, *args, **kwargs):
        print("# CommentViewset: create()")
        project_id = self.kwargs['project_id']
        issue_id = self.kwargs['issue_id']

        print("Project_id:", project_id, ", Issue_id:", issue_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        issue = Issue.objects.get(id=issue_id, project_id=project_id)
        serializer.validated_data['issue'] = issue

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # 16. GET - Retrieve the list of all comments related to a problem
    def get_queryset(self):
        print("# CommentViewset: get()")

        project_id = self.kwargs['project_id']
        issue_id = self.kwargs['issue_id']
        comment_id = self.kwargs.get('pk')

        if ( comment_id == None ):
            print("# Results are filtered by project_id and issue_id.")
            queryset = Comment.objects.filter(issue__project_id=project_id, issue_id=issue_id)    
        else:
            print("No filter because 'comment_id' is set.")
            queryset = Comment.objects.all()

        return queryset

    # 17. PUT -  Edit a comment
    def update(self, request, *args, **kwargs):
        print("# CommentViewset: update()")
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # 18. DELETE - Delete a comment
    def destroy(self, request, *args, **kwargs):
        print("# CommentViewset: destroy()")
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 19. GET - Get a comment via its id
    def retrieve(self, request, *args, **kwargs):
        print("# CommentViewset: retrieve()")
           
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
