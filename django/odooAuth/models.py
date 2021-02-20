from django.db import models
from django.contrib.auth.backends import BaseBackend
from accounts.models import UserManager, User
from odoo.odoo import Odoo

odoo = Odoo()

class OdooBackend (BaseBackend):

    def authenticate(self, request, username=None, password=None, isOdooUser=False):
        if isOdooUser:
            user = self.authenticateOdooUser(request, username, password)
            return user
        else:
            user = self.authenticatePartner(request, username, password)
            return user

    def authenticatePartner(self, request, username=None, password=None):
        odoo.connect()
        user = None
        encodedData = odoo.searchPartnerByBirthdate(password)
        print(encodedData)
        for i in encodedData:
            dataDB = tuple(i.items())
            print("[DEBUG] Input email :"+username+" | Email gathered from db : "+dataDB[2][1])
            print("[DEBUG] ID gathered from db : "+str(dataDB[0][1]))
            if username == dataDB[2][1]:
                user = User.objects.create_user(
                    username, dataDB[0][1], dataDB[1][1], False, False)
        return user

    def authenticateOdooUser(self, request, usename=None, password=None):
        return None


