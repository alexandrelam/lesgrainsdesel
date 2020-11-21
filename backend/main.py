from odoo import Odoo

odoo = Odoo()

odoo.setCommonEndpoint()
print(odoo.version())
