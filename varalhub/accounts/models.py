
from random import randint
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.template.loader import get_template


######################################### Custom User Model Functionality ###########
# create a custom query set to override the default
class UserQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class UserManager(BaseUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model,using=self._db)

    def all(self):
        return self.get_queryset()

    def activeUsers(self):
        return self.get_queryset().active()   

    def create_user(self,email,username=None,password=None,country=None,is_active = True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        # if not username:
        #     raise ValueError("Users must have a full name")

        user_obj = self.model(
            email = self.normalize_email(email),
            username = username
        )  

        user_obj.set_password(password) #this method can also be used to  change password  
        user_obj.country = country
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,username=None,password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            is_staff=True
        )
        return user  

    def create_superuser(self, email,username=None,password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=True) #can login
    country = models.CharField(max_length=255,blank=True,null=True)
    has_subscription = models.BooleanField(default=False) #superuser
    staff = models.BooleanField(default=False) #staff user/ non superuser
    admin = models.BooleanField(default=False) #superuser
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' #default username
    # 
    REQUIRED_FIELDS =[]

    objects = UserManager() 

    def __str__(self):
        return self.email

    def get_name(self):
        if self.username:
            return self.username
        return self.email

    def get_short_name(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self, app_label):
        return True 

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
