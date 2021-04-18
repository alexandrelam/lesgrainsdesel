from django.db import models
from django.contrib.auth.backends import BaseBackend
from accounts.models import UserManager, User
from odoo.odoo import Odoo

class OdooBackend (BaseBackend):

    def authenticate(self, request, username=None, password=None, isOdooUser=False):
        if isOdooUser:
            user = self.authenticateOdooUser(request, username, password)
            return user
        else:
            user = self.authenticatePartner(request, username, password)
            return user

    def authenticatePartner(self, request, username=None, password=None):
        odoo = Odoo('admin', 'admin')
        odoo.connect()
        password = odoo.formatDate(password)
        print("date = "+password)
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

    def authenticateOdooUser(self, request, username=None, password=None):
        user = None
        odoo = Odoo(username, password)
        success = odoo.connect()
        if success == 1 and not odoo.getOdooAdminUid() == -1 :
                user = User.objects.create_user(
                           username, odoo.getOdooPartnerUid(username), odoo.getOdooName(username), True, True) 
        return user 


