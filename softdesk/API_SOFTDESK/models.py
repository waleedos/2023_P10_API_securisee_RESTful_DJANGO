from django.db import models
from django.contrib.auth.models import User 


# 
# "Project" model
#
# 
class Project(models.Model):

    TYPE = (
        ('PYTHON', 'Python3'),
        ('DJANGO', 'DJANGO'),
        ('REACT', 'React'),
        ('BACKEND', 'Back-end'),
        ('FRONTEND', 'Front-end'),
        ('IOS', 'IOS'),
        ('ANDROID', 'Android'),
    )

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPE)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_author")
    contributors = models.ManyToManyField(User, through="Contributor")

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


#
# "Contributor" model
# 
class Contributor(models.Model):

    PERMISSIONS = (
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    )

    permissions = models.CharField(max_length=255, choices=PERMISSIONS)
    role = models.CharField(max_length=255, null=True, blank=True, default='')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Contributors"
 

#
# "Issue" model
# 
class Issue(models.Model):
    PRIORITY = (
                    ('LOW', 'Low'),
                    ('MEDIUM', 'Medium'),
                    ('HIGH', 'High')
    )

    TAG = (
                ('BUG', 'Bug'),
                ('IMPROUVMENT', 'Improuvment'),
                ('TASK', 'Task')
    )

    STATUS = (
                ('TODO', 'Todo'),
                ('CURRENT', 'Current'),
                ('END', 'End')
    )

    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, choices=TAG)
    priority = models.CharField(max_length=255, choices=PRIORITY)
    status = models.CharField(max_length=255, choices=STATUS)
    created_time = models.DateTimeField(auto_now_add=True) 
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issue_assignee')

    class Meta:
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.title


#
# "Comment" model
# 
class Comment(models.Model):
    description = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now = True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.description
