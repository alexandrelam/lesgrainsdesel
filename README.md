# Repo test où on apprend des choses

## Frontend

Début de l'intégration du landing.

![landing_v1](https://user-images.githubusercontent.com/25727549/100433402-4fb10f00-309b-11eb-8ab8-60b95dfea113.PNG)
![landingmedium](https://user-images.githubusercontent.com/25727549/100482533-02af5600-30f8-11eb-9774-68abeeeb34c6.PNG)
![ladingmediummenun](https://user-images.githubusercontent.com/25727549/100482536-0347ec80-30f8-11eb-96cf-7718a34d3280.PNG)
![landingphone](https://user-images.githubusercontent.com/25727549/100482535-0347ec80-30f8-11eb-9fc2-6b3e7061504f.PNG)

**Important** il faut télécharger et ajouter dans le dossier frontend `frontend\fontawesome-free-5.15.1-web`.

### Installation des icônes

1. Téléchargez le dossier suivant : https://use.fontawesome.com/releases/v5.15.1/fontawesome-free-5.15.1-web.zip
2. Dézipez et placez le dossier dans le dossier frontend (lesgrainsdesel/frontend/fontawesome-free-5.15.1-web)

### Todo

- [x] Intégration du la maquette landing pour les écrans de tailles grandes et moyennes
- [x] Navbar hamburger
- [x] Media queries pour les différentes tailles de pages
- [ ] Bonus ! Changer le bouton du menu hamburger pour fermer
- [ ] Finir les maquettes des autres pages

## Backend

Création d'un premier niveau d'abstraction avec la class Odoo.

Voir le code simplifié dans le fichier `main.py`. Avant d'exécuter n'oubliez pas de rajouter des au moins 2 évènements dans odoo.

Le fichier `test.py` ne sert à rien pas besoin de checker

Les fichiers `.json` servent d'exemple pour montrer les différentes propriétés disponibles pour les membres et évènements.

### Exemple d'utilisation

```python
from odoo import Odoo

odoo = Odoo()

# connect() permet de set les endpoints common et
# object ainsi que d'obtenir le uid
odoo.connect()

# exemple : on cherche l'evenement avec un id de 2
#           et on affiche que la propriete name et
#           l organisateur de l evenement

# Ne pas oublier de rajouter au moins 2 evenements
print(odoo.searchRead("event.event", [["id", "=", 2]], ["name", "organizer_id"]))
```

### Todo

- [x] Connection facilité
- [ ] Trouver où est situé le système de points
- [ ] Trouver comment marche l'identification des membres de la coopération et des admins sur odoo

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
