# Repo test où on apprend des choses

## Frontend

Début de l'intégration du landing.

**Important** il faut télécharger et ajouter dans le dossier frontend `frontend\fontawesome-free-5.15.1-web`.

## Backend

Création d'un premier niveau d'abstraction avec la class Odoo.

Voir le code simplifié dans le fichier `main.py`. Avant d'exécuter n'oubliez pas de rajouter des au moins 2 évènements dans odoo.

Le fichier `test.py` ne sert à rien pas besoin de checker

# Getting Started

Ce guide va vous apprendre à installer et configurer Docker pour le faire fonctionner avec foodcoop, une version de Odoo avec des addons supplémentaires.

> Ce guide est écrit pour les utilisateurs de windows 10. Si vous êtes sur Linux vous devriez savoir vous débrouiller sans lire ce guide.

## Installation de Docker

Cliquez sur le lien suivant pour télécharger [Docker](https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe).
Avant de l'installer, assurez-vous d'avoir activé les fonctionnalités Hyper-V et Container de Windows.

Une fois intallé, lancez Docker pour vérifier qu'il n'y ait pas d'erreurs. Vous pouvez alors suivre le tutoriel de 2 minutes pour comprendre les bases de l'outil.

## Installation de Git

---

Tutoriel étape par étape pour installer git :
https://phoenixnap.com/kb/how-to-install-git-windows

---

Téléchargez GIT pour windows en cliquand sur ce [lien](https://git-scm.com/downloads).

Installez git et lancez le pour le configurer.

`git config --global user.name "FIRST_NAME LAST_NAME"`

`git config --global user.email "MY_NAME@example.com"`

## Configuration de FoodCoop avec Docker

Une fois que vous avez configuré git, déplacez vous dans le dossier de votre choix puis clonez le répo _foodcoop_.

`git clone https://gitlab.com/lgds/foodcoops`

Rendez-vous dans le dossier dans lequel vous avez cloné le répo foodcoop.

Exécutez la commande `docker-compose up` pour démarrer le conteneur de l'application.

## Lancement de Odoo

Une fois le conteneur de foodcoop lancé, rendez-vous sur `http://127.0.0.1:8069`

- Email : admin

- Mot de passe : admin

A partir de là, installez les applications coop-account et coop-shift.

Après avoir suivi ces étapes, vous pourrez accéder à la base de données avec python.

Pour comprendre comment se connecter avec python checkez le fichier `main.py` dans le dossier backend
