from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_("email"), max_length=254,unique=True)
    phone_number = models.CharField(_("phone number"), max_length=11,unique=True)
    full_name = models.CharField(_("full name"), max_length=255)
    is_active = models.BooleanField(_("is active"), default=True)
    is_admin = models.BooleanField(_("is admin"), default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email","full_name"]
    
    def __str__(self):
        return self.email
    

    
    @property
    def is_staff(self):
        return self.is_admin
    

class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11,unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"
