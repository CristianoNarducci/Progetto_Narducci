from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class userManagement(BaseUserManager):
    def create_user(self, email, age, username, password=None):
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)

        if not username:
            msg = 'This username is not valid'
            raise ValueError(msg)

        if not age:
            msg = 'Please Verify Your DOB'
            raise ValueError(msg)

        user = self.model(email=self.normalize_email(email), username=username, age=age)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,username=None,age=None):
        user = self.create_user(email=self.normalize_email(email),username=username,age=age,password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user




# Create your models here.
class Profile(AbstractBaseUser):
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=200,unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','age']
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    songs = models.ManyToManyField('songs.Song',blank=True)

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value

    objects = userManagement()
