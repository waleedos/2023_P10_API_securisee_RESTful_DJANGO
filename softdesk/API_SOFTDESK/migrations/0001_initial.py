# Generated by Django 4.2.5 on 2023-09-27 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions', models.CharField(choices=[('admin', 'Administrator'), ('member', 'Member'), ('guest', 'Guest')], max_length=255)),
                ('role', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contributors',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('BACKEND', 'Back-end'), ('FRONTEND', 'Front-end'), ('IOS', 'IOS'), ('ANDROID', 'Android')], max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_author', to=settings.AUTH_USER_MODEL)),
                ('contributors', models.ManyToManyField(through='API_SOFTDESK.Contributor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('tag', models.CharField(choices=[('BUG', 'Bug'), ('IMPROUVMENT', 'Improuvment'), ('TASK', 'Task')], max_length=255)),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], max_length=255)),
                ('status', models.CharField(choices=[('TODO', 'Todo'), ('CURRENT', 'Current'), ('END', 'End')], max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_SOFTDESK.project')),
            ],
            options={
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_SOFTDESK.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_SOFTDESK.issue')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]