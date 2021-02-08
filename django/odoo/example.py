from odoo import Odoo
import json

odoo = Odoo()

odoo.connect()

# exemple : on cherche l'evenement avec un id de 2
#           et on affiche que la propriete name et
#           l organisateur de l evenement

# Ne pas oublier de rajouter au moins 2 evenements
#print(odoo.searchRead("event.event", [["id", "=", 2]], ["name", "organizer_id"]))
# exemple : sans filtre, on affiche tous les evenements
# verifier bien que l'id de la personne existe sinon
# changez l id

#print(odoo.searchRead("res.partner", [],
#                    ["name", "id", "birthdate"]))


result = odoo.searchPartnerByBirthdate("1995-03-07")
data = result[0]
output = tuple(data.items())
print(output)
print(output[1][1])

print(type(result))

print(odoo.searchPartnerByName("Test1"))
#odoo.createEvent("event_test5", "2020-12-28 20:18:18",
#                 "2020-12-29 20:18:18", 6)
