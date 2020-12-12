# -*- encoding: utf-8 -*-
from openerp import SUPERUSER_ID
from openerp.modules.registry import RegistryManager


def migrate(cr, version):
    if not version:
        return
    # registry = RegistryManager.get(cr.dbname)
    if module_is_installed(cr, 'website'):
        install_module(cr, 'website_server_mode')


def module_is_installed(cr, module):
    registry = RegistryManager.get(cr.dbname)
    model = registry['ir.module.module']
    module_ids = model.search(
        cr, SUPERUSER_ID,
        [('name', '=', module), ('state', '=', 'installed')], {})
    if module_ids:
        return True
    else:
        return False


def install_module(cr, module):
    registry = RegistryManager.get(cr.dbname)
    model = registry['ir.module.module']
    module_ids = model.search(
        cr, SUPERUSER_ID,
        [('name', '=', module)], {})
    model.button_install(
        cr, SUPERUSER_ID, module_ids, {})
