from odoo import Odoo

odoo = Odoo()

odoo.connect()

print(odoo.searchRead("event.event", [], ["name"]))
