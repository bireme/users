#! coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from utils.models import *

class Generic(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(_("created"), default=datetime.now())
    updated = models.DateTimeField(_("updated"), default=datetime.now())
    creator = models.ForeignKey(User, null=True, blank=True, related_name="+")
    updater = models.ForeignKey(User, null=True, blank=True, related_name="+")

    def save(self):
        self.updated = datetime.now()
        super(Generic, self).save()


class Profile(models.Model):

    DEGREE_CHOICES = (
        ('basic education', _('Basic Education')),
        ('high school', _('High School')),
        ('technical studies', _('Technical Studies')),
        ('graduate study', _('Graduate Study')),
        ('specialization', _('Specialization')),
        ("professional master's degree", _("Professional Master's Degree")),
        ("master's degree", _("Master's Degree")),
        ("doctorate", _('Doctorate')),
        ("mba", _('MBA')),
        ("post doctorate", _('Post Doctorate')),
        ("phd", _('PHD')),
    )

    GENDER_CHOICES = (
        ('m', _('Male')),
        ('f', _('Female')),
    )

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    user = models.OneToOneField(User, verbose_name="user") # allow extension of default django User
    degree = models.CharField(_("degree"), max_length=255, blank=True, null=True, choices=DEGREE_CHOICES)
    country = models.ForeignKey(Country, verbose_name=_("country"), default=30)
    gender = models.CharField(_("gender"), max_length=1, choices=GENDER_CHOICES)

# creates automatically and profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

post_save.connect(create_profile, sender=User, dispatch_uid="some.unique.string.id")