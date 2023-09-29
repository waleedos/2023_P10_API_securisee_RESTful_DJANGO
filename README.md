<h1 align="center">OpenClassrooms Project N°10</h1>
<h2 align="center">Créez une API sécurisée RESTful en utilisant Django REST</h1>

![Logo softdesk](https://raw.githubusercontent.com/waleedos/2023_P10_API_securisee_RESTful_DJANGO/main/Mission/softdesk-logo.png)


# SOFTDESK - Système de suivi des problèmes
Application pour signaler et suivre les problèmes techniques des entreprises clientes en B2B.

## Technologies
Python
Django
Django Rest Framework


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
[POSTMAN DOCUMENTATION](https://documenter.getpostman.com/view/...)


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

## Importer la documentation Postman publiée, et pour cela, il existe 3 façons : 
### 1- Ouvrez votre navigateur vers la documentation Postman publiée :

[POSTMAN SOFTDESK COLLECTION ](https://app.getpostman.com/run-collection/30089525-9e9772b9-a8b7-4b86-b446-82b8cc05e55a?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D30089525-9e9772b9-a8b7-4b86-b446-82b8cc05e55a%26entityType%3Dcollection%26workspaceId%3Def0eb810-172d-4467-ab6c-6250b50b8496)

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

************************************************************************************************
### 1 Inscription d'un utilisateur (Enregistrement)

    |PERMISSIONS  |
    |-------------|
    |AllowAny     |

#### Exécution de la requête

    * Ouvrez Postman
    * Utilisez la méthode "POST"
    * URI           : /signup/
    * URL complete  : http://127.0.0.1:8000/API_SOFTDESK/signup/
    * En-têtes      : Aucun
    * Corps         : Brut - JSON


{
     "first_name": "Sebastien",
     "last_name": "Legrand",
     "email": "slegrad@softdesk.com",
     "username": "slegrand",
     "password": "xxxxxxxx"
}


    * Cliquez sur le bouton "Envoyer"
    * Postman lance la requête
    * Postman affiche le résultat et les données sérialisées

#### Résultat de la requête
    * Résultat : "Statut : 201 Créé"


    {
            "first_name": "Sebastien",
            "last_name": "Legrand",
            "username": "slegrand",                 
            "email": "slegrad@softdesk.com",
        "date_joined": "2023-09-28T08:03:14.395287Z"
    }
   
        
************************************************************************************************

