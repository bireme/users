#! coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models
from django.db.models.signals import post_save

from utils.models import Generic, Country, LANGUAGES_CHOICES

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

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    USER_TYPE_CHOICES = (
        ('basic', _('Basic')),
        ('advanced', _('Advanced')),
    )

    cooperative_center = models.ForeignKey("CooperativeCenter", verbose_name=_("Cooperative Center"), null=True, blank=True)
    user = models.OneToOneField(User, verbose_name="user") # allow extension of default django User
    type = models.CharField(_("type"), max_length=30, choices=USER_TYPE_CHOICES, default="basic")

    

# creates automatically and profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

post_save.connect(create_profile, sender=User, dispatch_uid="some.unique.string.id")