# Generated by Django 4.2.5 on 2023-09-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0002_project_contributors_alter_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='consent',
            field=models.BooleanField(default=False),
        ),
    ]