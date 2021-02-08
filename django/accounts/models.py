from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ..odoo.odoo import Odoo


odoo = Odoo()

class UserManager(BaseUserManager):
    def create_user(self, email, userId, isStaff=False, isAdmin=False):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email = self.normalize_email(email))
        user.userId = userId 
        user.isStaff=isStaff
        user.isAdmin=isAdmin
        return user


class User(AbstractBaseUser):
    userId = models.IntegerField 
    fullName = models.CharField()
    email = models.EmailField(max_length=255, unique=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','userId'] 

    objects = UserManager()

    def __str__(self):
        return self.email

    def getUserId(self):
        return self.userId

    def getFullName(self): 
        return self.fullName

    def isStaff(self): 
        return self.staff

    def isAdmin(self): 
        return self.admin



class OdooBackend (BaseBackend) :


    def authenticate(self, request, username=None, password=None, isOdooUser=False) :
        if isOdooUser :
            user = authenticateOdooUser(self, request, username, password)
            return user 
        else :
            user = authenticatePartner(self,request, username, password)
            return user



    def authenticatePartner(self, request, username=None, password=None) :
        odoo.connect()
        user = None
        encodedData = odoo.searchPartnerByBirthdate(password) 
        for i in encodedData:
            if username == tuple(i)[1][1]:
                user = UserManager.create_user(username, tuple(i)[0][1], False, False)
        
        return user 

    def authenticateOdooUser(self, request, usename=None, password=None):
        return None
