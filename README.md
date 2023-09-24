# A venir

python manage.py test softdesk
python manage.py test softdesk.test_permissions




### Optimisation des Requêtes
Pour optimiser les requêtes à la base de données, je peux utiliser select_related ou prefetch_related dans mes QuerySets. Par exemple, 
si j'ai une vue qui retourne une liste de projets et chaque projet a un auteur, je peux optimiser la requête comme suit :

