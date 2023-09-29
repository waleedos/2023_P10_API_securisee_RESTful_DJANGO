# Generated by Django 4.2.5 on 2023-09-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_SOFTDESK', '0002_alter_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('PYTHON', 'Python3'), ('DJANGO', 'Django'), ('REACT', 'React'), ('BACKEND', 'Back-end'), ('FRONTEND', 'Front-end'), ('IOS', 'IOS'), ('ANDROID', 'Android')], max_length=255),
        ),
    ]
