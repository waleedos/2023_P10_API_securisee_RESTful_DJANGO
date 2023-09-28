from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Project
from .models import Contributor
from .models import Issue
from .models import Comment


# Manage ManytoMany in django administration interface
# Documentation Django
# https://docs.djangoproject.com/en/dev/ref/contrib/admin/#working-with-many-to-many-intermediary-models
#

class ContributorsInline(admin.TabularInline):
    model = Contributor
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]
    readonly_fields = ('id', )


class IssueAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'id',)


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'id',)


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline]
    readonly_fields = ('id', )


# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Contributor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)

