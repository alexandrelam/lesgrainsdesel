# Event management with Odoo

Application integrated with the Odoo ERP initially developed to facilitate event management for the Les Grains de Sel cooperative supermarket.

![maquettelanding](https://user-images.githubusercontent.com/25727549/101214918-1e2cda80-367d-11eb-9a03-bcd34327ea61.PNG)

## Table of content

- [Getting started recommended](#getting-started-recommended)
  - [Prerequisite](#prerequisite)
  - [Installation](#installation)
  - [After installation](#after-installation)
- [Getting started (manual)](#getting-started-manual)
  - [Prerequisite](#prerequisite)
    - [Git](#git)
    - [Python3](#python3)
    - [Django and other dependancies](#django-and-other-dependancies)
    - [Docker](#docker)
  - [Start Django app](#start-django-app)
  - [Start Odoo](#start-odoo)
- [Backend](#backend)
  - [Exemple of use](#exemple-of-use)
  - [todo](#todo)

## Getting started recommended

### Prerequisite

- Docker
- Git

### Installation

1. `git clone https://github.com/alexandrelam/lesgrainsdesel `
2. **Renomer le dossier `lesgrainsdesel` en un autre nom !** (Odoo ne fonctionne pas lorsque le dossier s'appelle `lesgrainsdesel`)
3. Move to the right folder
4. `docker-compose up`
5. Get inside the docker container to execute the next commands
6. `python3 manage.py migrate`
7. `python3 manage.py initadmin` this commands create a superuser with the user and password set as `admin`
8. Run the app and go to the admin page (`http://localhost:8000/admin/`)
9. Create an event and add an `adherent` (note: images field are not required thanks to default values)
10. Login `http://localhost:8000/login` (email=username of createsuperuser || password is password of createsuperuser)
11. Enjoy !

#### After installation

- You can access the django app using `http://localhost:8000`
- You can access odoo using `http://localhost:8069`
- Once you login in odoo using `admin` as the login and password, you need to install the following apps in the following order : coop-shift then coop-membership

## Getting started (manual)

### Prerequisite

- git
- Python3 && pip3
- Django 3
- Docker with foodcoop [image](https://gitlab.com/lgds/foodcoops)

##### Git

1. Install git : https://phoenixnap.com/kb/how-to-install-git-windows.
2. In a console/terminal configure git using
   `git config --global user.name "FIRST_NAME LAST_NAME"`
   `git config --global user.email "MY_NAME@example.com"`

##### Python3

1. Install [python3](https://www.python.org/downloads/).
2. Add python to path during the installation process to use python et pip in a console/terminal.
3. **Optional** if python and pip wasn't added to path on windows follow the next step.
   3.1 Add python to path : https://geek-university.com/python/add-python-to-the-windows-path/.
   3.2 Add PIP to path : https://projects.raspberrypi.org/en/projects/using-pip-on-windows/4.
4. Check your installation. Try to execute the command `python` and `pip` in your console/terminal.

##### Django and other dependancies

1. Move to the `django` directory using `cd django`.
2. Install dependancies using the command : `pip install -r requirements.txt`

##### Docker

1. Install DockerHub from : https://docs.docker.com/docker-for-windows/install/.
2. Déplacez vous dans le dossier de votre choix puis clonez le répo _foodcoop_ : `git clone https://gitlab.com/lgds/foodcoops`
3. Rendez-vous dans le dossier dans lequel vous avez cloné le répo foodcoop.
4. Exécutez la commande `docker-compose up` pour démarrer le conteneur de l'application.

### Start Django app

1. Move to the folder `django`.
2. `python manage.py runserver`

### Start Odoo

Once the foodcoop container is launched, go to `http: //127.0.0.1: 8069`

- Email: admin

- Password: admin

From there, install the coop-account and coop-shift apps.

After following these steps, you will be able to access the database with python using `odoo.py`.

## Backend

Creation of a first level of abstraction with the Odoo class.

### Exemple of use

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
- [ ] Bouger `odoo.py` dans une autre app django
- [ ] Optimiser les images car loading trop long quand on sélectionne un événement
