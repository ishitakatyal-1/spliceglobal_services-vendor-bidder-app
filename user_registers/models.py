from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

import uuid


class UserRegistrarManager(BaseUserManager):
    def create_user(
        self,
        registrar_fname,
        registrar_lname,
        registrar_username,
        registrar_email,
        password=None,
        **extra_fields
    ):
        if not registrar_fname:
            raise ValueError("First Name is to be supplied for registration.")
        if not registrar_lname:
            raise ValueError("Last Name is to be supplied for registration.")
        if not registrar_username:
            raise ValueError("Username has to be supplied for login.")
        if not registrar_email:
            raise ValueError("Email has to be supplied for contact information.")
        user = self.model(
            registrar_fname=registrar_fname,
            registrar_lname=registrar_lname,
            registrar_username=registrar_username,
            registrar_email=self.normalize_email(registrar_email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        registrar_fname,
        registrar_lname,
        registrar_username,
        registrar_email,
        password=None,
        **extra_fields
    ):
        user = self.create_user(
            registrar_fname=registrar_fname,
            registrar_lname=registrar_lname,
            registrar_username=registrar_username,
            registrar_email=self.normalize_email(registrar_email),
            password=password,
        )
        user.registrar_superuser = True
        user.save(using=self._db)
        return user


class UserRegistrar(AbstractBaseUser):

    # User types pre-defined to vendor or bidders
    USER_TYPE = [("V", "Vendor"), ("B", "Bidder")]

    # User unique id fields
    registrar_s_num = models.AutoField(primary_key=True)
    registrar_id = models.UUIDField(default=uuid.uuid4, unique=True)
    registrar_username = models.CharField(max_length=20, unique=True)

    # User personal information for contacting him/her
    registrar_fname = models.CharField(max_length=50)
    registrar_lname = models.CharField(max_length=50)
    registrar_email = models.EmailField(
        max_length=200, unique=True, default="email@email.com"
    )
    registrar_phone = models.IntegerField(null=True, blank=True)

    # User essential details for record-purposes
    registrar_type = models.CharField(max_length=1, choices=USER_TYPE)
    registrar_superuser = models.BooleanField(default=False)
    registrar_active = models.BooleanField(default=True)
    registrar_created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "registrar_username"
    REQUIRED_FIELDS = [
        "registrar_fname",
        "registrar_lname",
        "registrar_email",
    ]

    objects = UserRegistrarManager()

    def __str__(self):
        return self.registrar_username

    class Meta:
        db_table = "Account_users"