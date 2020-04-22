from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, name, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)

        user = self.model(email=email, name=name, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, False, False, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, True, True, **extra_fields)


# noinspection SpellCheckingInspection
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, max_length=100)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    is_google_user = models.BooleanField(default=False)
    new_password = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text=u"Somente usuários ativos podem acessar.")
    is_staff = models.BooleanField(default=False,
                                   help_text=u"Somente membros da equipe tem acesso ao site administrativo.")
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    def __str__(self):
        return self.name + ' (' + self.email + ')'

    REQUIRED_FIELDS = ['name', 'email']
