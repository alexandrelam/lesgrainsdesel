.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========
Server Mode
===========

This modules disable some functions when running databases on odoo servers with
parameter server_mode = "some value"

It also disable crons for instances with server_mode value (NOTA: tal vez veamos que nos conviene usar cron activados en no prod, en este caso podemos desactivarlos en el odoo conf usando el entrypoint para que segun el tipo o algun parametro los desactive)

This module is also inherited by other modules so that you can disable
functionalities depending on server mode. To use it:

* import with: from openerp.addons.server_mode.mode import get_mode
* use it like following:
    * if mode() == 'test':
    * if mode() == 'develop'
    * if mode():
    ... etc


Installation
============

To install this module, you need to:

#. Just install this module

Configuration
=============

To configure this module, you need to:

#. Set a parameter on your odoo.conf file lie "server_mode = test"

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.adhoc.com.ar/

.. repo_id is available in https://github.com/OCA/maintainer-tools/blob/master/tools/repos_with_ids.txt
.. branch is "8.0" for example

Known issues / Roadmap
======================

* ...

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ingadhoc/{project_repo}/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------

* ADHOC SA: `Icon <http://fotos.subefotos.com/83fed853c1e15a8023b86b2b22d6145bo.png>`_.

Contributors
------------


Maintainer
----------

.. image:: http://fotos.subefotos.com/83fed853c1e15a8023b86b2b22d6145bo.png
   :alt: Odoo Community Association
   :target: https://www.adhoc.com.ar

This module is maintained by the ADHOC SA.

To contribute to this module, please visit https://www.adhoc.com.ar.