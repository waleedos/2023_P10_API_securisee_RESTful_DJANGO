<h1 align="center">OpenClassrooms Project N°10</h1>
<h2 align="center">Créez une API sécurisée RESTful en utilisant Django REST</h1>

![Logo softdesk](https://raw.githubusercontent.com/waleedos/2023_P10_API_securisee_RESTful_DJANGO/main/Mission/softdesk-logo.png)


# SOFTDESK - Système de suivi des problèmes
Application pour signaler et suivre les problèmes techniques des entreprises clientes en B2B.

## Technologies
* Python
* Django
* Django Rest Framework


## Contribuer au projet
SOFTDESK Système de suivi des problèmes est un projet open-source. N'hésitez pas à forker le code source et à contribuer avec vos propres fonctionnalités.

## Auteurs
L'équipe est composée de EL-WALID EL-KHABOU et de son mentor OpenClassRooms.

## Licence
Logiciel gratuit.

## Préparation à l'utilisation de l'API
Ce programme a été testé avec python Python 3.10.12


### Obtenir le code source du programme : Cloner l'API
``` 
git clone https://github.com/waleedos/2023_P10_API_securisee_RESTful_DJANGO.git
```

### Se déplacer dans le projet
```
cd softdesk
```

### Créer un environnement virtuel Python
```
python -m venv venv
```

### Activer l'environnement virtuel Python
```
source ./env/bin/activate
```

### Importer les modules
```
pip install -r requirements.txt
```

### Lancer le serveur Django
```
cd softdesk/
python manage.py runserver
```

## Documentation Postman pour Softdesk

Lien vers la documentation publiée de Postman :
[POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/30089525/2s9YJaYPpq)


## Installation de Postman

Téléchargez Postman depuis : `https://www.postman.com/downloads/`


### Exemple pour Linux (x64)
* Ouvrez votre navigateur : https://www.postman.com/downloads/
* Sélectionnez "Télécharger l'application de bureau pour Linux"
* Cliquez sur "Linux (x64)"
* Postman est téléchargé
* Déplacez l'application où vous le souhaitez
* Décompressez l'archive
```
tar xvzf postman-linux-x64.tar.gz
```
* Entrez dans le dossier Postman
```
cd Postman
```
* Lancez l'application Postman
```
./Postman
```

## Si vous voulez consulter mon Profil publique POSTMAN : 
[My POSTMAN PUBLIC PROFILE ](https://www.postman.com/ewekdev?tab=collections)


## Importer la documentation Postman publiée, et pour cela, il existe 3 façons : 
### 1- Ouvrez votre navigateur vers la documentation Postman publiée :

[POSTMAN SOFTDESK COLLECTION ](https://documenter.getpostman.com/view/30089525/2s9YJaYPpq)

### 2- Cliquez sur le bouton "Run in Postman" en haut à droite oubien sur le bouton suivant : 

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/30089525-9e9772b9-a8b7-4b86-b446-82b8cc05e55a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D30089525-9e9772b9-a8b7-4b86-b446-82b8cc05e55a%26entityType%3Dcollection%26workspaceId%3Def0eb810-172d-4467-ab6c-6250b50b8496)


* Sélectionnez l'application Postman locale
* Choisissez l'espace de travail pour importer la collection
* Cliquez sur "Importer"
* Cliquez sur "Collections"

Maintenant, vous pouvez voir la collection dans l'application Postman locale.

### 3- télécharger manuellement la collection de tests Postman .json : 
* ouvrez un terminal, et déplacez vous dans le dossier téléchargement : 
```
cd ~/Téléchargements
```

* Copiez/coller la commande suivante dans le terminal:
```
curl -O https://github.com/waleedos/2023_P10_API_securisee_RESTful_DJANGO/blob/main/Documents/SOFTDESK.postman_collection.json
```
* Maintenant, vous avez la collection dans votre dossier téléchargement, et vous pouvez l'importer directement depuis votre application locale Postman

## Comment faire
### Général
* Ouvrez l'application API de requête Postman
* Utilisez le (endpoint) pour vous inscrire à l'API
* Utilisez le (endpoint) pour vous connecter à l'API
* Utilisez les (endpoint) ...


### Détails de l'API
Cette partie est une table avec les détails des (endpoint) de l'API. 

#### ATTENTION : 
Si vous voulez clicker sur les liens existants dans le tableau suivant, il est impératif que votre environnement
virtuel soit activé, et que votre serveur est fonctionnel aussi : rappelez vous donc de le démarrer avec cette commande :
```
python manage.py runserver
```

| #  | Point d'accès API                                       | Méthode HTTP | URI                         | URL pour Cliquer                                                                 |
|----|---------------------------------------------------------|-------------|-----------------------------|----------------------------------------------------------------------------------|
| 1  | Inscription de l'utilisateur                            | POST        | `/signup/`                  | [Cliquez ici](http://127.0.0.1:8000/API_SOFTDESK/signup/)                |
| 2  | Connexion de l'utilisateur                              | POST        | `/login/`                   | [Cliquez ici](http://127.0.0.1:8000/API_SOFTDESK/login/)                 |
| 3  | Récupérer la liste de tous les projets liés à l'utilisateur connecté | GET | `/projects/`               | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/)              |
| 4  | Créer un projet                                         | POST        | `/projects/`                | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/)              |
| 5  | Récupérer les détails du projet via son ID              | GET         | `/projects/{id}/`           | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/)         |
| 6  | Mettre à jour un projet                                 | PUT         | `/projects/{id}/`           | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/)         |
| 7  | Supprimer un projet et ses problèmes                    | DELETE      | `/projects/{id}/`           | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/)         |
| 8  | Ajouter un collaborateur à un projet                    | POST        | `/projects/{id}/users/`     | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/users/)   |
| 9  | Récupérer la liste de tous les utilisateurs liés à un projet | GET      | `/projects/{id}/users/`     | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/users/)   |
| 10 | Retirer un utilisateur d'un projet                      | DELETE      | `/projects/{id}/users/{id}` | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/users/{id}/)|
| 11 | Récupérer la liste des problèmes liés à un projet       | GET         | `/projects/{id}/issues/`    | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/)  |
| 12 | Créer un problème dans un projet                        | POST        | `/projects/{id}/issues/`    | [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/)  |
| 13 | Mettre à jour un problème dans un projet                | PUT         | `/projects/{id}/issues/{id}`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/{id}/)|
| 14 | Supprimer un problème d'un projet                       | DELETE      | `/projects/{id}/issues/{id}`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/{id}/)|
| 15 | Créer des commentaires sur un problème                  | POST        | `/projects/{id}/issues/{id}/comments/`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/)|
| 16 | Récupérer la liste de tous les commentaires liés à un problème | GET    | `/projects/{id}/issues/{id}/comments/`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/)|
| 17 | Éditer un commentaire                                   | PUT         | `/projects/{id}/issues/{id}/comments/{id}`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/56/issues/{id}/comments/{id}/)|
| 18 | Supprimer un commentaire                                | DELETE      | `/projects/{id}/issues/{id}/comments/{id}`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/56/issues/{id}/comments/{id}/)|
| 19 | Obtenir un commentaire via son ID                        | GET         | `/projects/{id}/issues/{id}/comments/{id}`| [Cliquez ici](http://localhost:8000/API_SOFTDESK/projects/56/issues/{id}/comments/{id}/)|


## Exploration de nos (endpoint) un par un : 

========================================================================================

## 1 Inscription d'un utilisateur (Enregistrement)

    |PERMISSIONS  |
    |-------------|
    |AllowAny     |

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /signup/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/signup/
    * En-têtes      : Aucun
    * Corps         : Brut - JSON

```
{
     "first_name": "Sebastien",
     "last_name": "Legrand",
     "email": "slegrad@softdesk.com",
     "username": "slegrand",
     "password": "xxxxxxxx"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Créé"

```
{
        "first_name": "Sebastien",
        "last_name": "Legrand",
        "username": "slegrand",                 
        "email": "slegrad@softdesk.com",
        "date_joined": "2023-09-28T08:03:14.395287Z"
}
```   
        
========================================================================================

## 2 Connexion de l'utilisateur (signin) ou (login)

    |PERMISSIONS  |
    |-------------|
    |AllowAny     |

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /login/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/login/
    * En-têtes      : Aucun
    * Corps         : Brut - JSON

```
{
     "username": "slegrand",
     "password": "xxxxxxxx"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NjA4NTkwNSwiaWF0IjoxNjk1OTk5NTA1LCJqdGkiOiIzNDU4OWYyOGQ4NzQ0ZGU3YTgwZDNkYjk1NTBhNjg0YiIsInVzZXJfaWQiOjR9.RXz1Toll96yLkPKqRZHCt_CmuSy9X0VPzMPpuwXOU6o",

    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NTkxNTA1LCJpYXQiOjE2OTU5OTk1MDUsImp0aSI6ImIwNzg2MjQ2NGI0YjQwZTE4YmVhNGRkOTM5ODRhNzUxIiwidXNlcl9pZCI6NH0.bl0DEyRpy8NpEgy-DUA5AYdPucKzbF6Gdc7S9xdZfjk"
}
```   
        
========================================================================================

## 3 Créer un projet

    |PERMISSIONS        |
    |-------------------|
    |IsAuthenticated    |
    |-------------------|
    |PermissionProject  |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /project/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Brut - JSON

```
    { 
        "title": "PROJET_DE_FIXBUG_API",
        "description": "Description du projet FIXBUG-API",
        "type": "DJANGO"
    }
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Created"

```
{
    "id": 5,
    "author": 5,
    "title": "PROJET_DE_FIXBUG_API",
    "description": "Description du projet FIXBUG-API",
    "type": "DJANGO",
    "contributors": []
}
```   
    
  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Un projet n'est accessible qu'à son créateur et à ses contributeurs</td>
    </tr>
  </table>

========================================================================================

## 4  Récupérer la liste de tous les projets liés à l'utilisateur connecté

    |PERMISSIONS        |
    |-------------------|
    |IsAuthenticated    |
    |-------------------|
    |PermissionProject  |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /project/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 2,
    "author": 2,
    "title": "PROJECT_06 (Auteur can update a project - Do not delete)",
    "description": "This description will be update : UPDATED !",
    "type": "ANDROID",
    "contributors": [4, 5]
}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Un projet n'est accessible qu'à son créateur et ses contributeurs</td>
    </tr>
  </table>

========================================================================================

## 5 Récupérer les détails du projet via son ID

    |PERMISSIONS        |
    |-------------------|
    |IsAuthenticated    |
    |-------------------|
    |PermissionProject  |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /projects/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 5,
    "author": 5,
    "title": "PROJET_DE_FIXBUG_API",
    "description": "Description du projet FIXBUG-API",
    "type": "DJANGO",
    "contributors": []
}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Les projets ne sont visibles que par leur auteur ou contributeurs</td>
    </tr>
  </table>
  
========================================================================================

## 6 Mettre à jour un projet

    |PERMISSIONS        |
    |-------------------|
    |IsAuthenticated    |
    |-------------------|
    |PermissionProject  |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "put"
    * URI           : /projects/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Raw - JSON

```
{
    "title": "MISE À JOUR DU 1ER  PROJET CREE PAR mlegendre",
    "description": "This description is UPDATED !",
    "type": "PYTHON3",
    "author": "5"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 5,
    "author": 5,
    "title": "MISE À JOUR DU 1ER  PROJET CREE PAR mlegendre",
    "description": "This description is UPDATED !",
    "type": "PYTHON3",
    "contributors": []
}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur a la permission de mettre à jour un projet</td>
    </tr>
  </table>

========================================================================================

## 7 Supprimer un projet et ses problèmes

    |PERMISSIONS        |
    |-------------------|
    |IsAuthenticated    |
    |-------------------|
    |PermissionProject  |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "DELETE"
    * URI           : /projects/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 204 OK = Aucun Contenu"

```
{


}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur a la permission de supprimer un projet</td>
    </tr>
  </table>
        
========================================================================================

## 8 Ajouter un collaborateur à un projet

    |PERMISSIONS             |
    |------------------------|
    |IsAuthenticated         |
    |------------------------|
    |PermissionProjectsUsers |

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /projects/{id}/users/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Raw - JSON

```
{
    "user_id": "2",
    "permissions": "Member",
    "role": "contributeur"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Créé"

```
{
    "id": 6,
    "permissions": "Member",
    "role": "contributeur",
    "user": 2,
    "project": 5
}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur du projet est autorisé à ajouter un contributeur</td>
    </tr>
  </table>
        
========================================================================================

## 9 Récupérer la liste de tous les utilisateurs liés à un projet

    |PERMISSIONS             |
    |------------------------|
    |IsAuthenticated         |
    |------------------------|
    |PermissionProjectsUsers |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /projects/{id}/users/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/project/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 Ok"

```
{
    "id": 6,
    "permissions": "Member",
    "role": "contributeur",
    "user": 2,
    "project": 5
}
```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur du projet ou les contributeurs de ce dernier peuvent lister les utilisateurs liés à un projet</td>
    </tr>
  </table>
        
========================================================================================

## 10 Retirer un utilisateur d'un projet

    |PERMISSIONS             |
    |------------------------|
    |IsAuthenticated         |
    |------------------------|
    |PermissionProjectsUsers |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "DELETE"
    * URI           : /projects/{id}/users/{id}
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/users/{id}
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 204 Pas de contenu"

```


```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur du projet peut supprimer un utilisateur lié à un projet</td>
    </tr>
  </table>
        
========================================================================================

## 11 Créer un problème dans un projet

    |PERMISSIONS     |
    |----------------|
    |IsAuthenticated |
    |----------------|
    |PermissionIssue |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /projects/{id}/issues/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Raw - JSON

```
{
    "title": "Création de problème pour le projet créé par mlegendre",
    "desc": "Pour le projet N°5 créé par mlegendre",
    "tag":  "IMPROUVMENT",
    "priority": "LOW",
    "status": "CURRENT",
    "author": "5"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Créé"

```
{
    "id": 10,
    "project": 5,
    "assignee": 5,
    "title": "Création de problème pour le projet créé par mlegendre",
    "desc": "Pour le projet N°5 créé par mlegendre",
    "tag": "IMPROUVMENT",
    "priority": "LOW",
    "status": "CURRENT",
    "created_time": "2023-09-30T08:14:11.958125+02:00",
    "author": 5
}

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur et les contributeurs d'un projet peuvent créer des problèmes</td>
    </tr>
  </table>
        
========================================================================================

## 12 Récupérer la liste des problèmes liés à un projet

    |PERMISSIONS     |
    |----------------|
    |IsAuthenticated |
    |----------------|
    |PermissionIssue |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /projects/{id}/issues/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 5,
    "project": 2,
    "assignee": 2,
    "title": "Création de problème : l'auteur du projet peut créer un problème",
    "desc": "Nous mettons ici la Description du problème de l'auteur",
    "tag": "BUG",
    "priority": "MEDIUM",
    "status": "TODO",
    "created_time": "2023-09-28T13:02:20.078733+02:00",
    "author": 2
}

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur du projet ou ses contributeurs peuvent lister les les problèmes</td>
    </tr>
  </table>
        
========================================================================================

## 13 Mettre à jour un problème dans un projet

    |PERMISSIONS     |
    |----------------|
    |IsAuthenticated |
    |----------------|
    |PermissionIssue |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "PUT"
    * URI           : /projects/{id}/issues/{id}
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Brut - JSON

```
{
    "title": "Création de problème pour le projet créé par mlegendre, mis à jour par mleroi",
    "desc": "Pour le projet N°5 créé par mlegendre",
    "tag":  "IMPROUVMENT",
    "priority": "MEDIUM",
    "status": "CURRENT",
    "author": "5"
}
```

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 10,
    "project": 5,
    "assignee": 5,
    "title": "Création de problème pour le projet créé par mlegendre, mis à jour par mleroi",
    "desc": "Pour le projet N°5 créé par mlegendre",
    "tag": "IMPROUVMENT",
    "priority": "MEDIUM",
    "status": "CURRENT",
    "created_time": "2023-09-30T08:14:11.958125+02:00",
    "author": 5
}

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un probleme peut l'editer et le mettre à jour</td>
    </tr>
  </table>
        
========================================================================================

## 14 Supprimer un problème d'un projet

    |PERMISSIONS     |
    |----------------|
    |IsAuthenticated |
    |----------------|
    |PermissionIssue |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "DELETE"
    * URI           : /projects/{id}/issues/{id}
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 204 No Content"

```


```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un projet ou l'auteur d'un probleme peuvent supprimer ce dernier</td>
    </tr>
  </table>
        
========================================================================================

## 15 Créer des commentaires sur un problème

    |PERMISSIONS       |
    |------------------|
    |IsAuthenticated   |
    |------------------|
    |PermissionComment |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "POST"
    * URI           : /projects/{id}/issues/{id}/comments/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Brut - JSON

```
{
    "description": "L'auteur d'un projet et ses contributeurs peuvent commenter un des probleme de ce projet",
    "author": "2"
}

``` 

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Created"

```
{
    "id": 2,
    "issue": 9,
    "description": "L'auteur d'un projet peut commenter un des probleme de ce projet",
    "created_time": "2023-09-28T18:41:57.017156+02:00",
    "author": 2
}

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un projet ou ses contributeurs peuvent créer un commentaire sur un probleme</td>
    </tr>
  </table>
        
========================================================================================

## 16 Récupérer la liste de tous les commentaires liés à un problème

    |PERMISSIONS       |
    |------------------|
    |IsAuthenticated   |
    |------------------|
    |PermissionComment |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /projects/{id}/issues/{id}/comments/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
[
    {
        "id": 1,
        "issue": 9,
        "description": "Je suis juste un contributor de ce projet, et je peut commenter un de ses probleme",
        "created_time": "2023-09-28T18:39:33.193915+02:00",
        "author": 4
    },
    {
        "id": 2,
        "issue": 9,
        "description": "L'auteur d'un projet peut commenter un des probleme de ce projet",
        "created_time": "2023-09-28T18:41:57.017156+02:00",
        "author": 2
    }
]

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un projet ou ses contributeurs peuvent acceder à la liste des commentaire sur un probleme</td>
    </tr>
  </table>
        
========================================================================================

## 17 Modifier un commentaires sur un problème

    |PERMISSIONS       |
    |------------------|
    |IsAuthenticated   |
    |------------------|
    |PermissionComment |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "PUT"
    * URI           : /projects/{id}/issues/{id}/comments/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Brut - JSON

```
{
    "description": "Commentaire pour le projet N° 2 - probleme N° 9 changement du commentaire accepté car c'est l'auteur de ce dernier",
    "author": 4
}

``` 

    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```
{
    "id": 2,
    "issue": 9,
    "description": "Commentaire pour le projet N° 2 - probleme N° 9 changement du commentaire accepté car c'est l'auteur de ce dernier",
    "created_time": "2023-09-28T21:09:51.081702+02:00",
    "author": 4
}

```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un commentaire peut l'editer et le modifier</td>
    </tr>
  </table>
        
========================================================================================

## 18 Supprimer un commentaires

    |PERMISSIONS       |
    |------------------|
    |IsAuthenticated   |
    |------------------|
    |PermissionComment |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "DELETE"
    * URI           : /projects/{id}/issues/{id}/comments/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 204 No Content"

```


```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>Seul l'auteur d'un commentaire ou l'auteur du projet peuvent supprimer le commentaire</td>
    </tr>
  </table>
        
========================================================================================

## 19 Appeler et voir le commentaire par son ID

    |PERMISSIONS       |
    |------------------|
    |IsAuthenticated   |
    |------------------|
    |PermissionComment |    

#### Exécution de la requête

    * Ouvrez Postman
    * Méthode       : "GET"
    * URI           : /projects/{id}/issues/{id}/comments/{id}/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/projects/{id}/issues/{id}/comments/{id}/
    * En-têtes      : Authorization = Bearer [jeton d'accès]
    * Corps         : Aucun
    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 200 OK"

```


```   

  <table border="1">
    <tr>
      <th>CONCLUSIONS</th>
    </tr>
    <tr>
      <td>L'utilisateur doit être authentifié</td>
    </tr>
      <tr>
      <td>L'auteur d'un projet et tous les contributeurs de ce dernier peuvent peuvent voir un commentaire par son ID</td>
    </tr>
  </table>
        
========================================================================================