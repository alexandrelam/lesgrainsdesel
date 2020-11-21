from odoo import Odoo

odoo = Odoo()

odoo.connect()

# exemple : on cherche l'evenement avec un id de 2
#           et on affiche que la propriete name et
#           l organisateur de l evenement

# Ne pas oublier de rajouter au moins 2 evenements
print(odoo.searchRead("event.event", [
      ["id", "=", 2]], ["name", "organizer_id"]))

# exemple : sans filtre, on affiche tous les evenements
print(odoo.searchRead("event.event", [], ["name"]))
