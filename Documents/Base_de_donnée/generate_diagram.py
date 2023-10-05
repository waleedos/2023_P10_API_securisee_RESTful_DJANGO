import os
import django
from django.db import models as django_models  # Import spécifique pour éviter les conflits

# Configurez les paramètres de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'softdesk.settings')
django.setup()

from graphviz import Digraph
from API_SOFTDESK.models import Project, Contributor, Issue, Comment

# Initialiser Graphviz
dot = Digraph(comment='Database Schema')

# Liste des modèles
model_list = [Project, Contributor, Issue, Comment]  # Renommé pour éviter les conflits

# Parcourir tous les modèles
for model in model_list:
    dot.node(model.__name__)

    # Parcourir tous les champs du modèle
    for field in model._meta.get_fields():
        if field.is_relation:
            related_model = field.related_model.__name__
            relation_type = ''
            
            if isinstance(field, django_models.OneToOneField):
                relation_type = 'OneToOne'
            elif isinstance(field, django_models.ForeignKey):
                relation_type = 'ForeignKey'
            elif isinstance(field, django_models.ManyToManyField):
                relation_type = 'ManyToMany'
            
            label = f"{field.name}: {relation_type}"
            dot.edge(model.__name__, related_model, label=label)

# Générer le diagramme
dot.render('database_diagram', view=True)
