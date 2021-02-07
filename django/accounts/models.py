from django.db import models
from django.contrib.auth.backends import BaseBackend
from ..odoo.odoo import Odoo


odoo = Odoo()

class OdooBackend (BaseBackend) :
    def authenticate(self, request, username=None, password=None, isOdooUser=False) :
        if isOdooUser :
            user = authenticateOdooUser(self, request, username, password)
            return user 
        else :
            user = authenticatePartner(self,request, username, password)
            return user



    def authenticatePartner(self, request, username=None, password=None) :
       return user 
