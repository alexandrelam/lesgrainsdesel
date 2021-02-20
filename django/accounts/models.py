from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, userId, fullName, isStaff=False, isAdmin=False):
        if not email:
            raise ValueError("Users must have an email address")
        print("[DEBUG]Creating user with email : " + email)
        user = self.model(email=self.normalize_email(email))
        print("[DEBUG] User id = " + str(userId))
        user.userId = userId
        user.fullName = fullName
        user.isStaff = isStaff
        user.isAdmin = isAdmin
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userId = models.IntegerField(unique=True, primary_key=True)
    fullName = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'userId']

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
