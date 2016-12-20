from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.gis.db import models as geo
from django.core.mail import send_mail

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('Email address', unique=True)
    first_name = models.CharField('First name', max_length=64, blank=True)
    last_name = models.CharField('Last name', max_length=64, blank=True)
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 't_users'
        verbose_name_plural = 'Users'
        ordering = ('date_joined',)

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Item(models.Model):

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    img = models.ImageField(upload_to='items', blank=True, null=True)
    pub_date = models.DateTimeField('Date published', auto_now_add=True)
    pub_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = geo.PointField(blank=True, null=True)

    class Meta:
        db_table = 't_items'
        verbose_name_plural = 'Items'
        ordering = ('pub_date',)

    def little_description(self):
        return self.description[:100]

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=128)

    class Meta:
        db_table = 't_cities'
        verbose_name_plural = 'Cities'


class District(models.Model):

    name = models.CharField(max_length=64)
    poly = geo.PolygonField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_districts'
        verbose_name_plural = 'Districts'
