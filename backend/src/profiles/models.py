from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

class User(AbstractBaseUser):

    email = models.EmailField(_('Email address'), unique=True, max_length=255, null=False, blank=False)
    is_admin = models.BooleanField(_('Is admin'), default=False)
    is_staff = models.BooleanField(_('Is staff'), default=False)
    is_active = models.BooleanField(_('Is active'),default=True)
    created_date = models.DateTimeField(_('Date created'), auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])




