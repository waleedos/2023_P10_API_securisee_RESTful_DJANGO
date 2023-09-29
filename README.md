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

